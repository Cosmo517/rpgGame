"""
The following python file for a dijkstra map implementation
(also called flood map?) was used from the following:
https://github.com/HenrYxZ/dijkstra-map/tree/main

Modified slightly
"""

import numpy as np


def add_neighbors(closed, j, i):
    """
    Add neighbor pixels that are not in the closed map.
    Args:
        closed (ndarray): 2D binary array where true means being closed
        j (int): index of row for the pixel
        i (int): index of column for the pixel

    Returns:
        list: list of tuples with indices for the neighbor pixels not in closed
    """
    h, w = closed.shape
    rows = [j - 1, j, j + 1]
    cols = [i - 1, i, i + 1]

    # (i, j) (x, y)...
    # (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)


    neighbors = []

    if 0 <= j - 1 < h and 0 <= i < w and not closed[j-1][i]:
        closed[j - 1][i] = True
        neighbors.append((j - 1, i))
    if 0 <= j + 1 < h and 0 <= i < w and not closed[j + 1][i]:
        closed[j + 1][i] = True
        neighbors.append((j + 1, i))
    if 0 <= j < h and 0 <= i - 1 < w and not closed[j][i - 1]:
        closed[j][i - 1] = True
        neighbors.append((j, i - 1))
    if 0 <= j < h and 0 <= i + 1 < w and not closed[j][i + 1]:
        closed[j][i + 1] = True
        neighbors.append((j, i + 1))

    return neighbors


def dijkstra_map(input_map, walls_map=None, limit=0):
    """
    Create a Dijkstra map flood filling a given 2D map
    Args:
        input_map (ndarray): input 2D array
        walls_map (ndarray): a binary 2D array where true means a wall
        limit (int): after this limit it will stop flooding, is like max
            distance

    Returns:
        ndarray: 2D array with distances
    """
    h, w = input_map.shape
    # Initialize the new array with every pixel at limit distance
    new_arr = np.ones([h, w], dtype=int) * limit
    if walls_map is not None:
        closed = np.copy(walls_map)
    else:
        closed = np.zeros([h, w], dtype=bool)
    starting_pixels = []
    open_pixels = []
    total_pixels = h * w
    if not limit:
        limit = total_pixels
    # First pass: Add starting pixels and put them in closed
    for counter in range(h * w):
        i = counter % w
        j = counter // w
        if input_map[j][i] == 0:
            new_arr[j][i] = 0
            closed[j][i] = True
            starting_pixels.append((j, i))


    # Second pass: Add border to open
    for j, i in starting_pixels:
        open_pixels += add_neighbors(closed, j, i)
    # Third pass: Iterate filling in the open list
    counter = 1
    while counter < limit and open_pixels:
        next_open = []
        for j, i in open_pixels:
            new_arr[j][i] = counter
            next_open += add_neighbors(closed, j, i)
        open_pixels = next_open
        counter += 1
    # Last pass: flood last pixels
    for j, i in open_pixels:
        new_arr[j][i] = counter

    for i in range(h):
        for j in range(w):
            if walls_map[i][j]:
                new_arr[i][j] = 200

    return new_arr
