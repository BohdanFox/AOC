from Utils import read_data_as_numbers

positions = read_data_as_numbers(7)
min_distance = None
min_fuel = None
for i in range(max(positions) + 1):
    distances = [abs(position - i) for position in positions]
    distance = sum(distances)
    fuel = sum([(x * (x + 1)) // 2 for x in distances])
    if min_distance is None or distance < min_distance:
        min_distance = distance
    if min_fuel is None or fuel < min_fuel:
        min_fuel = fuel
print(min_distance)
print(min_fuel)
