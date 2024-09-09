#!/usr/bin/env python3

import json
import h5py
import numpy as np
import utils

ENABLE_GIF = True
if ENABLE_GIF:
    from PIL import Image

def load_json(file):
    '''
    Load parameters from `input.json`

    ### Parameters

    file : str
        Path to the input.json file

    ### Returns

    width : int
    height : int
    time : int
    viscosity : int
    splats : list
    '''
    with open(file,"r") as ipt:
        events = json.load(ipt)
        width = events["width"]
        height = events["height"]
        time = events["time"]
        viscosity = events["viscosity"]
        splats = events["splats"]
    return width, height, time, viscosity, splats

def save_hdf5(file, velocity, dyes):
    '''
    Save data to an HDF5 file

    ### Parameters

    file : str
        Path to the HDF5 file
    data : np.array
        Data to be saved
    '''
    with h5py.File(file, 'w') as f:
        f.create_dataset('velocity', data=velocity)
        f.create_dataset('dyes', data=dyes)
        f.close()

def grad(f):
    '''
    Calculate the gradient of a scalar field f at any position (x, y)

    ### Parameters

    f : np.array
        Scalar field

    ### Returns

    g : np.array
        Gradient of f at any position (x, y).
        g[0] is the x-component, g[1] is the y-component
    '''

    # Calculate the gradient of f
    g_x = (np.roll(f, -1, axis=0) - np.roll(f, 1, axis=0)) / 2
    g_y = (np.roll(f, -1, axis=1) - np.roll(f, 1, axis=1)) / 2

    return np.stack([g_x, g_y], axis=-1)

def diverg(f):
    '''
    Calculate the divergence of a vector field f at position (x, y)

    ### Parameters

    f : np.array

    ### Returns

    d : np.array
        Divergence of f at any position (x, y)
    '''

    # Calculate the divergence of f
    dfx_dx = (np.roll(f[...,0], -1,axis=0) - np.roll(f[...,0], 1, axis=0)) / 2
    dfy_dy = (np.roll(f[...,1], -1,axis=1) - np.roll(f[...,1], 1, axis=1)) / 2

    return dfx_dx + dfy_dy

class Fluid:
    def __init__(self, height, width, viscosity):
        self.height = height
        self.width = width

        # Velocity field, self.velocity[0] is the x-component, self.velocity[1] is the y-component
        self.velocity = np.zeros((height, width, 2), dtype=np.double)

        # Dye density field. Has a maximum value of 1. Corresponding to RBG colors.
        self.dyes = np.zeros((height, width, 3), dtype=np.double)

        self.viscosity = viscosity

        print("[INFO] Preparing velocity diffusion solver...")
        # Instantiate velocity diffusion solver
        self.diffusion_solver = \
                utils.build_poisson_solver(self.height, self.width, 1, -viscosity, -1)
        print("[INFO] Preparing pressure solver...")
        # Instantiate pressure solver
        self.pressure_solver = \
                utils.build_poisson_solver(self.height, self.width, 0, 1, 1)

    def splat(self, center, r, accel, dyes):
        for dx in range(-r, r + 1):
            for dy in range(-r, r + 1):
                x = center[0] + dx
                y = center[1] + dy

                if x < 0 or x >= self.height or y < 0 or y >= self.width:
                    continue

                if np.linalg.norm([dx, dy]) <= r:
                    self.velocity[x, y] += accel
                    self.dyes[x, y] = np.clip(self.dyes[x, y] + dyes, None, 1)

    def read_field(self, f, i, j):
        ni = np.clip(i, 0, self.height - 1).astype(int)
        nj = np.clip(j, 0, self.width - 1).astype(int)
        return f[ni][nj]

    def bilinear(self, f, x, y):
        '''
        Perform bilinear interpolation on a scalar field f at position (x, y)

        ### Parameters

        f : np.array
            Scalar field
        x : float
            x-coordinate
        y : float
            y-coordinate

        ### Returns

        interpolated_value : float
            Interpolated value at position (x, y)
        '''
        int_x = int(x)
        int_y = int(y)
        delta_x = x - int_x
        delta_y = y - int_y

        f_x0y0 = self.read_field(f, int_x, int_y)
        f_x1y0 = self.read_field(f, int_x + 1, int_y)
        f_x0y1 = self.read_field(f, int_x, int_y + 1)
        f_x1y1 = self.read_field(f, int_x + 1, int_y + 1)

        interpolated_value = (1 - delta_y) * ((1 - delta_x) * f_x0y0 + delta_x * f_x1y0) + \
                                  delta_y * ((1 - delta_x) * f_x0y1 + delta_x * f_x1y1)

        return interpolated_value

    def copy_to_boundary(self, f, factor):
        '''
        Copy the boundary of the field f to the boundary of the field f

        ### Parameters

        f : np.array
            Field to copy the boundary from
        factor : float
            Factor to multiply the boundary values with

        ### Returns

        None
        '''
        f[0, :] = f[1, :] * factor
        f[-1, :] = f[-2, :] * factor
        f[:, 0] = f[:, 1] * factor
        f[:, -1] = f[:, -2] * factor

    def step(self):
        # =========
        # Advection
        # =========
        # Implement advection transformation
        advected_velocity = np.zeros_like(self.velocity)
        advected_dyes    = np.zeros_like(self.dyes)

        for i in range(self.height):
            for j in range(self.width):
                x = i - self.velocity[i, j, 0]
                y = j - self.velocity[i, j, 1]
                advected_velocity[i, j] = self.bilinear(self.velocity, x, y)
                advected_dyes[i, j] = self.bilinear(self.dyes, x, y)

        self.velocity = advected_velocity
        self.dyes = advected_dyes

        # Reset dye density field outside the boundary
        self.copy_to_boundary(self.dyes, 0)
        # Ensures boundary conditions for our velocity field
        self.copy_to_boundary(advected_velocity, -1)

        # ===============
        # Speed diffusion
        # ===============
        # Implement speed diffusion transformation
        diffused_velocity = np.zeros_like(self.velocity)
        diffused_velocity[:, :, 0] = self.diffusion_solver(
            self.velocity[:, :, 0].flatten()
        ).reshape(self.height, self.width)
        diffused_velocity[:, :, 1] = self.diffusion_solver(
            self.velocity[:, :, 1].flatten()
        ).reshape(self.height, self.width)

        self.velocity = diffused_velocity
        # Ensures boundary conditions for our velocity field
        self.copy_to_boundary(self.velocity, -1)

        # ==========
        # Projection
        # ==========
        # Implement projection transformation
        # 1. Solve \nabla^2 q = diverg(diffused_velocity) using the pre-constructed solver
        # 2. Ensure q's boundary condition with self.copy_to_boundary
        # 3. Subtract grad(q) from diffused_velocity
        # pressure = self.pressure_solver(diverg(diffused_velocity).flatten())\
        #           .reshape(self.height, self.width)
        pressure= self.pressure_solver(
            diverg(diffused_velocity).flatten()
        ).reshape(self.height, self.width)
        self.copy_to_boundary(pressure, 1)
        self.velocity= diffused_velocity - grad(pressure)

        # Ensures boundary conditions for our velocity field one last time
        self.copy_to_boundary(self.velocity, -1)

def main():
    # Load parameters from `input.json`
    input_json = "input.json"
    width, height, time, viscosity, splats = load_json(input_json)

    # Simulator
    sim = Fluid(height, width, viscosity)

    # GIF frames
    frames = []

    for step in range(0, time):
        print(f"[INFO] Step: {step}")

        # Create splats in the simulation domain
        for splat in splats:
            if splat["time_from"] <= step < splat["time_to"]:
                sim.splat(
                    splat["center"], splat["radius"], splat["accel"], splat["dyes"]
                )

        # Calculate new velocity / dye density after this time slice
        sim.step()

        # Render GIF
        if ENABLE_GIF:
            frames.append(Image.fromarray((sim.dyes * 255).astype("uint8")))
            frames[0].save(
                "output.gif",
                save_all=True,
                append_images=frames[1:],
                duration=30,
                loop=0,
            )

    print("[INFO] Done!")

    # Save data to an HDF5 file
    output_h5 = "output.hdf5"
    save_hdf5(output_h5, sim.velocity, sim.dyes)

if __name__ == "__main__":
    main()
