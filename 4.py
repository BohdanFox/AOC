from Utils import read_data

raw_data = read_data(4)
random_numbers = [int(number) for number in raw_data[0].split(",")]
boards = []
for i in range(1, len(raw_data), 6):
    board = []
    for j in range(1, 6):
        board.append([int(number) for number in raw_data[i+j].split(" ") if number.isdigit()])
    boards.append(board)

def is_board_winning(board, numbers):
    for row in board:
        if set(row) <= set(numbers):
            return True
    for column in zip(*board):
        if set(column) <= set(numbers):
            return True
    return False

result = None
board_won = [False] * len(boards)
for index, number in enumerate(random_numbers):
    for board_index, board in enumerate(boards):
        selected_numbers = random_numbers[:index+1]
        if is_board_winning(board, selected_numbers):
            if not board_won[board_index]:
                flat_board = [item for sublist in board for item in sublist]
                remaining_sum = sum(set(flat_board) - set(selected_numbers))
                result = number * remaining_sum
                
                if not any(board_won):
                    first_result = result
                board_won[board_index] = True
                if all(board_won):
                    last_result = result
print(first_result)
print(last_result)