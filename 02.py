from Utils import read_data

data = read_data(2)
depth_1 = 0
depth_2 = 0
horizontal_position = 0
aim = 0

for entry in data:
    command = entry.split(" ")
    if len(command) == 2:
        command[1] = int(command[1])
        if command[0] == "forward":
            horizontal_position += command[1]
            depth_2 += aim * command[1]
        if command[0] == "down":
            aim += command[1]
            depth_1 += command[1]
        if command[0] == "up":
            aim -= command[1]
            depth_1 -= command[1]

print(horizontal_position * depth_1)
print(horizontal_position * depth_2)
