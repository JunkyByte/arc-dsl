import numpy as np
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


colors = [
    "#000000",  # symbol_0: black
    "#0074D9",  # symbol_1: blue
    "#FF4136",  # symbol_2: red
    "#2ECC40",  # symbol_3: green
    "#FFDC00",  # symbol_4: yellow
    "#AAAAAA",  # symbol_5: grey
    "#F012BE",  # symbol_6: fuschia
    "#FF851B",  # symbol_7: orange
    "#7FDBFF",  # symbol_8: teal
    "#870C25",  # symbol_9: brown
]
CMAP = mcolors.ListedColormap(colors)


def plot_single_grid(I):
    grid_array = np.array(I, dtype=int)

    _, ax = plt.subplots()
    ax.imshow(grid_array, cmap=CMAP, aspect='equal')

    # Add grid lines
    ax.set_xticks(np.arange(grid_array.shape[1]) - 0.5, minor=True)
    ax.set_yticks(np.arange(grid_array.shape[0]) - 0.5, minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)

    # Hide major ticks
    ax.tick_params(which="major", bottom=False, left=False)

    # Hide the axis labels
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()


def plot_two_grids(I1, I2):
    grid_array1 = np.array(I1, dtype=int)
    grid_array2 = np.array(I2, dtype=int)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    ax1.imshow(grid_array1, cmap=CMAP, aspect='equal')
    ax2.imshow(grid_array2, cmap=CMAP, aspect='equal')

    # Add grid lines to both
    for ax, grid_array in zip([ax1, ax2], [grid_array1, grid_array2]):
        ax.set_xticks(np.arange(grid_array.shape[1]) - 0.5, minor=True)
        ax.set_yticks(np.arange(grid_array.shape[0]) - 0.5, minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=2)

        # Hide major ticks
        ax.tick_params(which="major", bottom=False, left=False)

        # Hide the axis labels
        ax.set_xticks([])
        ax.set_yticks([])

    plt.show()


def plot_three_grids(Input, Output, Exp_Output):
    grid_array1 = np.array(Input, dtype=int)
    grid_array2 = np.array(Output, dtype=int)
    grid_array3 = np.array(Exp_Output, dtype=int)
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    ax1.imshow(grid_array1, cmap=CMAP, aspect='equal')
    ax2.imshow(grid_array2, cmap=CMAP, aspect='equal')
    ax3.imshow(grid_array3, cmap=CMAP, aspect='equal')

    # Add grid lines to all
    for ax, grid_array in zip([ax1, ax2, ax3], [grid_array1, grid_array2, grid_array3]):
        ax.set_xticks(np.arange(grid_array.shape[1]) - 0.5, minor=True)
        ax.set_yticks(np.arange(grid_array.shape[0]) - 0.5, minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=2)

        # Hide major ticks
        ax.tick_params(which="major", bottom=False, left=False)

        # Hide the axis labels
        ax.set_xticks([])
        ax.set_yticks([])

    plt.show()
