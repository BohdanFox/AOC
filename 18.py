from typing import Tuple
from Utils import read_data

def addition(first_snailfish_number: str, second_snailfish_number: str) -> str:
    result = f"[{first_snailfish_number},{second_snailfish_number}]"
    while True:
        has_exploded, result = try_to_explode(result)
        if has_exploded:
            continue
        has_splitted, result = try_to_split(result)
        if has_splitted:
            continue
        break
    return result

def try_to_explode(snailfish_number: str) -> Tuple[bool, str]:
    for index in range(len(snailfish_number)):
        pass

def try_to_split(snailfish_number: str) -> Tuple[bool, str]:
    pass

data = read_data(18)
result = data[0]
for entry in data[1:]:
    result = addition(result, entry)
print(result)
