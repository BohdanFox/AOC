from Utils import read_data
import numpy as np
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

ENLARGED_MATRIX_COEF = (5, 5)

def calculate_minimal_wight_path(matrix, calculate_first_element = False):
    grid = Grid(matrix=matrix)
    start = grid.node(0, 0)
    end = grid.node(matrix.shape[0] - 1, matrix.shape[1] - 1)
    path, _ = AStarFinder().find_path(start, end, grid)

    result = sum([matrix[x, y] for (y, x) in path])
    if not calculate_first_element:
        result -= matrix[0, 0]
    return result


raw_data = read_data(15)
original_matrix = [[int(char) for char in row] for row in raw_data]
original_matrix = np.array(original_matrix)

original_matrix_result = calculate_minimal_wight_path(original_matrix)
print(original_matrix_result)

enlarged_matrix = np.zeros(np.multiply(original_matrix.shape, ENLARGED_MATRIX_COEF), dtype=int)
for sub_matrix_index_x in range(ENLARGED_MATRIX_COEF[0]):
    for index_x_indide_submatrix in range(original_matrix.shape[0]):
        x = sub_matrix_index_x * original_matrix.shape[0] + index_x_indide_submatrix

        for sub_matrix_index_y in range(ENLARGED_MATRIX_COEF[1]):
            for index_y_indide_submatrix in range(original_matrix.shape[1]):
                y = sub_matrix_index_y * original_matrix.shape[1] + index_y_indide_submatrix
                
                original_value = original_matrix[index_x_indide_submatrix, index_y_indide_submatrix]
                new_value = original_value + sub_matrix_index_x + sub_matrix_index_y
                adjusted_value = (new_value - 1) % 9 + 1
                enlarged_matrix[x, y] = adjusted_value
                
enlarged_matrix_result = calculate_minimal_wight_path(enlarged_matrix)
print(enlarged_matrix_result)
