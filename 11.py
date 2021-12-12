from Utils import read_data
import numpy as np

ITERATIONS_TO_COUNT_CELLS_EXCESS = 100


def update_cell(data, row_index, column_index):
    cells_exceeded_critical_value = 0
    data[row_index][column_index] += 1

    if data[row_index][column_index] == 10:
        cells_exceeded_critical_value += 1
        for row_change in range(-1, 2):
            for column_change in range(-1, 2):
                row_range = range(len(data))
                column_range = range(len(data[1]))

                new_row = row_index + row_change
                new_column = column_index + column_change

                if (
                    (row_change, column_change) != (0, 0)
                    and (new_row in row_range)
                    and (new_column in column_range)
                ):
                    cells_exceeded_critical_value += update_cell(
                        data, new_row, new_column
                    )
    return cells_exceeded_critical_value


raw_data = read_data(11)
data = [[int(char) for char in row] for row in raw_data]
synchronization_point = None
cells_exceeded_critical_value = 0

iterations = 0
while iterations < ITERATIONS_TO_COUNT_CELLS_EXCESS or synchronization_point is None:
    for row_index in range(len(data)):
        for column_index in range(len(data[row_index])):
            cells_exceeded = update_cell(data, row_index, column_index)
            if iterations < ITERATIONS_TO_COUNT_CELLS_EXCESS:
                cells_exceeded_critical_value += cells_exceeded
    data = [[cell if cell < 10 else 0 for cell in row] for row in data]
    iterations += 1
    if np.all(np.array(data) == 0):
        synchronization_point = iterations
        break

print(cells_exceeded_critical_value)
print(synchronization_point)
