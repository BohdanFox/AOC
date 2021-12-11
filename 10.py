from Utils import read_data
from statistics import median

OPENING_BRACKETS =             ["(", "[", "{",  "<"  ]
CLOSING_BRACKETS =             [")", "]", "}",  ">"  ]
POINTS_FOR_INCORRECT_BRACKET = [3,   57,  1197, 25137]
POINTS_FOR_AUTOCOMPLETE =      [1,   2,   3,    4    ]

def calculate_autocomplete_points(bracket_index_stack):
    result = 0
    for bracket_index in reversed(bracket_index_stack):
        result *= 5
        result += POINTS_FOR_AUTOCOMPLETE[bracket_index]
    return result

data = read_data(10)
corrupt_brackets_points_sum = 0
autocomplete_points_results = []

for entry in data:
    is_corrupt = False
    bracket_index_stack = []
    for symbol in entry:
        if symbol in OPENING_BRACKETS:
            bracket_index = OPENING_BRACKETS.index(symbol)
            bracket_index_stack.append(bracket_index)
        elif symbol in CLOSING_BRACKETS:
            found_bracket_index = CLOSING_BRACKETS.index(symbol)
            expected_bracket_index = bracket_index_stack.pop()
            if found_bracket_index != expected_bracket_index:
                is_corrupt = True
                corrupt_brackets_points_sum += POINTS_FOR_INCORRECT_BRACKET[found_bracket_index]
                break
    if not is_corrupt:
        autocomplete_points_result = calculate_autocomplete_points(bracket_index_stack)
        autocomplete_points_results.append(autocomplete_points_result)

print(corrupt_brackets_points_sum)
print(median(autocomplete_points_results))
