#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.ndimage import zoom
import utils

def split_data(data):
    '''
    Read data from the input dictionary.

    Parameters:
    data (dict): A dictionary containing the data.

    Returns:
    tuple: A tuple containing the terrain, wind, and precipitation data.
    '''
    terrain_meta = data['terrain']['metadata']
    terrain_origin = np.array(terrain_meta['origin'])
    terrain_pixel = np.array(terrain_meta['pixel'])
    terrain_data = np.array(data['terrain']['data'])
    wind_meta = data['wind']['metadata']
    wind_origin = np.array(wind_meta['origin'])
    wind_pixel = np.array(wind_meta['pixel'])
    wind_data = np.array(data['wind']['data'])
    precipitation_meta = data['precipitation']['metadata']
    precipitation_data = np.array(data['precipitation']['data'])
    precipitation_origin = np.array(precipitation_meta['origin'])
    precipitation_pixel = np.array(precipitation_meta['pixel'])

    terrain = [terrain_origin, terrain_pixel, terrain_data]
    wind = [wind_origin, wind_pixel, wind_data]
    precipitation = [precipitation_origin, precipitation_pixel, precipitation_data]

    return terrain, wind, precipitation

def select_data(terrain, wind, precipitation):
    '''
    Select data needed for plotting.

    Parameters:
    terrain (list): A list containing the terrain metadata and data.
    wind (list): A list containing the wind metadata and data.
    precipitation (list): A list containing the precipitation metadata and data.

    Returns:
    None
    terrain (list): A list containing the terrain metadata and data.
    wind (list): A list containing the wind metadata and data.
    precipitation (list): A list containing the precipitation metadata and data.

    Useful infomation:
        The metadata.origin of these data is the center of the plot, and the
        metadata.pixel is the size of each pixel.This function is to select the
        data needed (in a selected boudary) for plotting.
    '''
    # Define the boundary and size of the plot
    boundary = (40, 41, 116, 117.5)
    size = (300, 300)

    def select_boundary(origin, pixel, data, boundary, size):
        '''
        Select the boundary of the data.

        Parameters:
        origin (list): The origin of the data.
        pixel (list): The size of each pixel.
        data (np.array): The data.
        boundary (tuple): The boundary of the plot.
        size (tuple): The size of the plot.

        Returns:
        np.array: The selected data.
        '''
        latitude_min, latitude_max, longitude_min, longitude_max = boundary
        x_size, y_size = size
        latitude_val1 = int(abs((origin[0] - latitude_min) / pixel[0]))
        latitude_val2 = int(abs((origin[0] - latitude_max) / pixel[0]))
        longitude_val1 = int(abs((origin[1] - longitude_min) / pixel[1]))
        longitude_val2 = int(abs((origin[1] - longitude_max) / pixel[1]))

        latitude_min = min(latitude_val1, latitude_val2)
        latitude_max = max(latitude_val1, latitude_val2)
        longitude_min = min(longitude_val1, longitude_val2)
        longitude_max = max(longitude_val1, longitude_val2)

        data_selected = data[latitude_min:latitude_max, longitude_min:longitude_max]

        # Calculate the zoom factors needed to resize the selected data to the desired size
        zoom_factor_lat = x_size / data_selected.shape[0]
        zoom_factor_lon = y_size / data_selected.shape[1]

        # Use scipy's zoom function to resize the data
        if len(data_selected.shape) == 3:
            data_resized = zoom(data_selected, (zoom_factor_lat, zoom_factor_lon, 1), order=3)
        else:
            data_resized = zoom(data_selected, (zoom_factor_lat, zoom_factor_lon), order=3)

        return data_resized

    # Read the data
    terrain_origin, terrain_pixel, terrain_data = terrain
    wind_origin, wind_pixel, wind_data = wind
    precipitation_origin, precipitation_pixel, precipitation_data = precipitation

    # Select data needed.
    #    Here we need to select the data within the boundary. The center of the plot is
    #    the origin of the data (latitude, longitude). The size of each pixel is the pixel
    #    of the data. The selected data should be in the boundary of the plot. And this
    #    function is to select the data needed for plotting.

    terrain_out = select_boundary(
            terrain_origin, terrain_pixel, terrain_data, boundary, size)
    wind_out = select_boundary(
            wind_origin, wind_pixel, wind_data, boundary, size)
    precipitation_out = select_boundary(
            precipitation_origin, precipitation_pixel, precipitation_data, boundary, size)

    return terrain_out, wind_out, precipitation_out

def plot_data(terrain, wind, precipitation):
    '''
    Plot the terrain, wind, and precipitation data.

    Parameters:
    terrain (np.array): The terrain data.
    wind (np.array): The wind data.
    precipitation (np.array): The precipitation data.

    Returns:
    None
    '''

    axis = [40, 41, 116, 117.5]

    with PdfPages('terrain.pdf') as pdf:
        fig, axs = plt.subplots(2, 2, figsize=(14, 10))

        # Plot Terrain
        ctf = axs[0, 0].contourf(terrain, 5, cmap='terrain')
        fig.colorbar(ctf, ax=axs[0, 0])
        x_labels = np.linspace(axis[0], axis[1], 5)
        y_labels = np.linspace(axis[2], axis[3], 5)
        axs[0, 0].set_xticks(np.linspace(0, len(terrain[0]), 5))
        axs[0, 0].set_yticks(np.linspace(0, len(terrain), 5))
        axs[0, 0].set_xticklabels([f"{label:.1f}" for label in x_labels])
        axs[0, 0].set_yticklabels([f"{label:.1f}" for label in y_labels])
        axs[0, 0].set_xlabel('Longitude')
        axs[0, 0].set_ylabel('Latitude')
        axs[0, 0].set_title('Terrain')

        # Plot Wind
        x = np.arange(0, 300, 10)
        y = np.arange(0, 300, 10)
        Q = axs[0, 1].quiver(x, y, wind[::10, ::10, 0], wind[::10, ::10, 1], color='black')
        axs[0, 1].quiverkey(Q, 0.75, 1.03, 1, label='1 m/s', labelpos='E')
        axs[0, 1].set_xticks(np.linspace(0, len(wind[0]), 5))
        axs[0, 1].set_yticks(np.linspace(0, len(wind), 5))
        axs[0, 1].set_xticklabels([f"{label:.1f}" for label in x_labels])
        axs[0, 1].set_yticklabels([f"{label:.1f}" for label in y_labels])
        axs[0, 1].set_xlabel('Longitude')
        axs[0, 1].set_ylabel('Latitude')
        axs[0, 1].set_title('Wind')

        # Plot Precipitation
        ctf = axs[1, 0].contourf(precipitation, 100, cmap='Blues')
        fig.colorbar(ctf, ax=axs[1, 0])
        axs[1, 0].set_xticks(np.linspace(0, len(precipitation[0]), 5))
        axs[1, 0].set_yticks(np.linspace(0, len(precipitation), 5))
        axs[1, 0].set_xticklabels([f"{label:.1f}" for label in x_labels])
        axs[1, 0].set_yticklabels([f"{label:.1f}" for label in y_labels])
        axs[1, 0].set_xlabel('Longitude')
        axs[1, 0].set_ylabel('Latitude')
        axs[1, 0].set_title('Precipitation')

        # Plot all datasets
        axs[1, 1].contour(terrain, 5, cmap='terrain')
        ctf = axs[1, 1].contourf(precipitation, 100, cmap='Blues', alpha=0.5)
        fig.colorbar(ctf, ax=axs[1, 1])
        axs[1, 1].quiver(x, y, wind[::10, ::10, 0], wind[::10, ::10, 1], color='black')
        axs[1, 1].set_xticks(np.linspace(0, len(terrain[0]), 5))
        axs[1, 1].set_yticks(np.linspace(0, len(terrain), 5))
        axs[1, 1].set_xticklabels([f"{label:.1f}" for label in x_labels])
        axs[1, 1].set_yticklabels([f"{label:.1f}" for label in y_labels])
        axs[1, 1].set_xlabel('Longitude')
        axs[1, 1].set_ylabel('Latitude')
        axs[1, 1].set_title('All datasets')

        # save the figure to the pdf
        pdf.savefig(fig)
        plt.close()

def main():
    '''
    Main function to read data and plot the terrain, wind, and precipitation data.
    '''
    data = utils.read_data()
    terrain, wind, precipitation = split_data(data)
    terrain, wind, precipitation = select_data(terrain, wind, precipitation)
    plot_data(terrain, wind, precipitation)

if __name__ == "__main__":
    main()
