from Utils import read_data

BINARY_LENGTH = 12

def calculate_most_least_common(data, index):
    counter = 0
    for entry in data:
        if entry[index] == "0":
            counter -=1
        if entry[index] == "1":
            counter +=1
    if counter >= 0:
        return "1", "0"
    else:
        return "0", "1"

data = read_data(3)

gamma_rate = ""
epsilon_rate = ""
for index in range(BINARY_LENGTH):
    most_common, least_common = calculate_most_least_common(data, index)
    gamma_rate += most_common
    epsilon_rate += least_common
result = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(result)


oxygen_rating_candidates = data
CO2_rating_candidates = data

for index in range(BINARY_LENGTH):
    most_common, _ = calculate_most_least_common(oxygen_rating_candidates, index)
    oxygen_rating_candidates = [entry for entry in oxygen_rating_candidates if entry[index] == most_common]
    if len(oxygen_rating_candidates) == 1:
        oxygen_rating = oxygen_rating_candidates[0]
        break

for index in range(BINARY_LENGTH):
    _, least_common = calculate_most_least_common(CO2_rating_candidates, index)
    CO2_rating_candidates = [entry for entry in CO2_rating_candidates if entry[index] == least_common]
    if len(CO2_rating_candidates) == 1:
        CO2_rating = CO2_rating_candidates[0]
        break
    
result = int(oxygen_rating, 2) * int(CO2_rating, 2)
print(result)
