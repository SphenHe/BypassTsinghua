import numpy as np
import matplotlib.pyplot as plt

# Constants
epsilon_0 = 8.854187817e-12  # Vacuum permittivity, F/m
e = 1.602176634e-19  # Elementary charge, C

# Functions to calculate contour lines
def log_lambda_D_values(lambdas, T_e):
    return np.log10(T_e) + np.log10(epsilon_0 / (lambdas**2 * e**2))

def log_N_D_values(N_Ds, T_e):
    return 3 * np.log10(T_e) + np.log10(epsilon_0**(3/2) / (N_Ds**(2/3) * e**6))

# Define range
n_e_values = np.logspace(6, 25, num=200)
T_e_values = np.logspace(-2, 5, num=200)

# Create mesh grid
T_e_grid, n_e_grid = np.meshgrid(T_e_values, n_e_values)

# Calculate contour lines
lambda_D_contour = log_lambda_D_values(1e-5, T_e_grid)  # Example Debye length
N_D_contour = log_N_D_values(1e10, T_e_grid)  # Example number of particles

# Plot contour lines
plt.figure(figsize=(10, 8))
CS_lambda = plt.contour(np.log10(T_e_grid), np.log10(n_e_grid), np.log10(n_e_grid) - lambda_D_contour, levels=10, colors='b', linestyles='dashed', linewidths=1)
CS_N_D = plt.contour(np.log10(T_e_grid), np.log10(n_e_grid), np.log10(n_e_grid) - N_D_contour, levels=10, colors='r', linewidths=1)

plt.clabel(CS_lambda, inline=True, fontsize=8, fmt='%.1f')
plt.clabel(CS_N_D, inline=True, fontsize=8, fmt='%.1f')

# Mark each point
points = {
    "Fusion Reactor": (21, 4),
    "Fusion Experiment (Ring)": (19, 2),
    "Fusion Experiment (Confinement)": (23, 3),
    "Ionosphere": (11, np.log10(0.05)),
    "Glow Discharge": (14, np.log10(2)),
    "Flame": (14, np.log10(0.1)),
    "Dusty Plasma": (17, np.log10(0.2)),
    "Interstellar Space": (6, np.log10(0.01))
}

for label, (log_ne, log_Te) in points.items():
    plt.scatter(log_Te, log_ne, label=label)

plt.xlabel(r'$\log_{10}(T_e)$ [eV]')
plt.ylabel(r'$\log_{10}(n_e)$ [m$^{-3}$]')
plt.xlim(-2, 5)
plt.ylim(6, 25)
plt.title('Plasma $n_e-T_e$ Diagram')
plt.legend()
plt.grid(True)
plt.savefig("./../img/1.pdf")
# plt.show()
