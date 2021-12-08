from Utils import read_data_as_numbers

positions = read_data_as_numbers(7)
min_result = None
for i in range(max(positions) + 1):
    result = sum([abs(position - i) for position in positions])
    if min_result is None or result < min_result:
        min_result = result
print(min_result)