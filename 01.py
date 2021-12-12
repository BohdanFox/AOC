from Utils import read_data_as_numbers

def calculate_increases(data, window_size):
    count = 0
    for i in range(1, len(data) - window_size + 1):
        previous_sum = sum(data[i - 1:i + window_size - 1])
        current_sum = sum(data[i:i + window_size])
        if previous_sum < current_sum:
            count += 1
    return count

data = read_data_as_numbers(1)
print(calculate_increases(data, 1))
print(calculate_increases(data, 3))
