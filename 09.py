from Utils import read_data
from collections import Counter

def get_neighbors(matrix, i, j):
    result = []
    if i > 0:
        result.append(matrix[i-1][j])
    if i+1 < len(matrix):
        result.append(matrix[i+1][j])
    if j > 0:
        result.append(matrix[i][j-1])
    if j+1 < len(matrix[0]):
        result.append(matrix[i][j+1])
    return result

result_sum = 0
raw_data = read_data(9)
data = [[int(char) for char in row] for row in raw_data]
for row_index, row in enumerate(data):
    for column_index, current_cell in enumerate(row):
        if current_cell < min(get_neighbors(data, row_index, column_index)):
            result_sum += 1 + current_cell
print(result_sum)

def get_neighbors_with_indexes(matrix, i, j):
    result = []
    if i > 0:
        result.append((i-1, j, matrix[i-1][j]))
    if i+1 < len(matrix):
        result.append((i+1, j, matrix[i+1][j]))
    if j > 0:
        result.append((i, j-1, matrix[i][j-1]))
    if j+1 < len(matrix[0]):
        result.append((i, j+1, matrix[i][j+1]))
    return result

result_sum = 0
raw_data = read_data(9)
data = [[int(char) for char in row] for row in raw_data]
basin_number = [(len(data[0]) * [-1]) for _ in range(len(data))]
for row_index, row in enumerate(data):
    for column_index, current_cell in enumerate(row):
        if current_cell == 9:
            continue
        neighbors = get_neighbors_with_indexes(data, row_index, column_index)
        for neighbor in neighbors:
            neighbor_row = neighbor[0]
            neighbor_column = neighbor[1]
            neighbor_value = neighbor[2]
            neighbor_basin = basin_number[neighbor_row][neighbor_column]
            if neighbor_basin != -1:
                current_cell_basin = basin_number[row_index][column_index]
                if current_cell_basin == -1:
                    basin_number[row_index][column_index] = neighbor_basin
                else:
                    basin_number = [[cell if cell != neighbor_basin else current_cell_basin for cell in row] for row in basin_number]
        if basin_number[row_index][column_index] == -1:
            basin_number[row_index][column_index] = max(max(x) for x in basin_number) + 1

flat_basin_number = [item for sublist in basin_number for item in sublist if item != -1]
counts = Counter(flat_basin_number).most_common(3)
result = 1
for _, x in counts:
    result *= x
print(result)
