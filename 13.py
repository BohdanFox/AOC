from Utils import read_data
import numpy as np


def fold_matrix(folds, matrix):
    for fold in folds:
        if fold[0] == "x":
            for x in range(fold[1]):
                for y in range(matrix.shape[1]):
                    matrix[x, y] = matrix[x, y] or matrix[matrix.shape[0] - x - 1, y]
            matrix = matrix[0 : fold[1], :]
        if fold[0] == "y":
            for x in range(matrix.shape[0]):
                for y in range(fold[1]):
                    matrix[x, y] = matrix[x, y] or matrix[x, matrix.shape[1] - y - 1]
            matrix = matrix[:, 0 : fold[1]]
    return matrix


unparsed_data = read_data(13)
border_index = unparsed_data.index("")
unparsed_dots = [entry.split(",") for entry in unparsed_data[:border_index]]
dots = [(int(x), int(y)) for x, y in unparsed_dots]
unparsed_folds = [entry.split("=") for entry in unparsed_data[border_index + 1 :]]
folds = [
    (dimension.replace("fold along ", ""), int(value))
    for dimension, value in unparsed_folds
]

max_x = max([x for x, y in dots])
max_y = max([y for x, y in dots])
matrix = np.full((max_x + 1, max_y + 1), False, dtype=bool)
for dot in dots:
    matrix[dot[0], dot[1]] = True

matrix_after_first_fold = fold_matrix(folds[0:1], matrix[:])
print(matrix_after_first_fold.sum())

finished_matrix = fold_matrix(folds, matrix[:])
for y in range(finished_matrix.shape[1]):
    for x in range(finished_matrix.shape[0]):
        if finished_matrix[x, y]:
            print("█", end="")
        else:
            print(" ", end="")
    print()
