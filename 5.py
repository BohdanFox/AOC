from Utils import read_data, read_data_as_numbers

required_size = max(read_data_as_numbers(5)) + 1
classic_diagram = [(required_size * [0]) for _ in range(required_size)]
diagram_with_diagonals = [(required_size * [0]) for _ in range(required_size)]

for entry in read_data(5):
    (x1, y1), (x2, y2) = [point.split(",") for point in entry.split(" -> ")]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    x_change = x2 - x1
    if x_change >= 0:
        x_direction = 1
    else:
        x_direction = -1

    y_change = y2 - y1
    if y_change >= 0:
        y_direction = 1
    else:
        y_direction = -1

    if x1 == x2 or y1 == y2:
        for i in range(x1, x2 + x_direction, x_direction):    
            for j in range(y1, y2 + y_direction, y_direction):
                classic_diagram[i][j] += 1
                diagram_with_diagonals[i][j] += 1
    elif abs(x_change) == abs(y_change):
        for i, j in zip(range(x1, x2 + x_direction, x_direction), 
                        range(y1, y2 + y_direction, y_direction)):
            diagram_with_diagonals[i][j] += 1

print(sum([1 for sublist in classic_diagram for item in sublist if item > 1]))
print(sum([1 for sublist in diagram_with_diagonals for item in sublist if item > 1]))