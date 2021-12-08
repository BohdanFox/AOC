import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data(number_from_one):
    result = []
    with open(os.path.join(__location__, f"Data By Day/{number_from_one}.txt")) as file:
        result = file.readlines()
        result = [line.rstrip() for line in result]
    return result

def read_data_as_numbers(number_from_one):
    result = []
    with open(os.path.join(__location__, f"Data By Day/{number_from_one}.txt")) as file:
        while (line := file.readline().rstrip()):
            try:
                number = int(line)
                result.append(number)
            except ValueError:
                pass
    return result