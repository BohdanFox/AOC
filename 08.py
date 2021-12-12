import itertools
from Utils import read_data

data = read_data(8)
result = 0
for entry in data:
    first_part, second_part = [part.split(" ") for part in entry.split(" | ")]
    result += sum([1 for elem in second_part if len(elem) == 2 or len(elem) == 3 or len(elem) == 4 or len(elem) == 7])
print(result)

def calculate_word_adter_permutation(permutation, word):
    word = word.replace("a", permutation[0])
    word = word.replace("b", permutation[1])
    word = word.replace("c", permutation[2])
    word = word.replace("d", permutation[3])
    word = word.replace("e", permutation[4])
    word = word.replace("f", permutation[5])
    word = word.replace("g", permutation[6])
    word = ''.join(sorted(word))
    return word

final_sum = 0
data = read_data(8)
for entry in data:
    original_numbers = ["ABCEFG", "CF", "ACDEG", "ACDFG", "BCDF", "ABDFG", "ABDEFG", "ACF", "ABCDEFG", "ABCDFG"]
    first_part, second_part = [part.split(" ") for part in entry.split(" | ")]
    first_part = [''.join(sorted(word)) for word in first_part]
    second_part = [''.join(sorted(word)) for word in second_part]
    possible_permutations = list(itertools.permutations("ABCDEFG"))
    for permutation in possible_permutations:
        changed_numbers = [calculate_word_adter_permutation(permutation, word) for word in first_part]
        if set(changed_numbers) == set(original_numbers):
            result = ""
            for word in second_part:
                word = calculate_word_adter_permutation(permutation, word)
                number = original_numbers.index(word)
                result += str(number)
            final_sum += int(result)
print(final_sum)
