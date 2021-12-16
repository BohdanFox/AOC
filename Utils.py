import os
import re
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data(file_number):
    result = []
    with open(os.path.join(__location__, f"Data By Day/{format(file_number, '02d')}.txt")) as file:
        result = file.readlines()
        result = [line.rstrip() for line in result]
    return result

def read_data_as_numbers(file_number, base=10, by_separate_characacters=False):
    result = []
    with open(os.path.join(__location__, f"Data By Day/{format(file_number, '02d')}.txt")) as file:
        while (line := file.readline().rstrip()):
            if by_separate_characacters:
                number_list = line
            else:
                number_list = re.split('\W+', line)
            for number_as_str in number_list:
                try:
                    number = int(number_as_str, base)
                    result.append(number)
                except ValueError:
                    pass
    return result
