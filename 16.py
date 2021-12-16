from typing import List
from Utils import read_data_as_numbers
import numpy as np

class Transmission:
    __binary_string: str
    __index: int
    __final_value: int
    __packet_versions: List

    @property
    def packet_versions(self):
        return self.__packet_versions

    @property
    def final_value(self):
        return self.__final_value

    def __init__(self, binary_str) -> None:
        self.__binary_string = binary_str
        self.__packet_versions = []
        self.__index = 0
        self.__final_value = self.__read_packet(True)

    def __read_packet(self, top_level=False):
        sub_packets = []

        packet_version = self.__read_new_binary_number(3)
        self.__packet_versions.append(packet_version)

        packet_type_id = self.__read_new_binary_number(3)
        if packet_type_id == 4:
            packet_bits = ""
            first_bit_is_zero = False
            while not first_bit_is_zero:
                binary_packet = self.__read_new_binary_number(5, False)
                first_bit_is_zero = binary_packet[0] == "0"
                packet_bits += binary_packet[1:]
            return int(packet_bits, 2)
        
        length_type_ID = self.__read_new_binary_number(1)
        if length_type_ID == 0:                
            sub_packets_lengths = self.__read_new_binary_number(15)
            sub_packets_end_index = self.__index + sub_packets_lengths
            while self.__index < sub_packets_end_index:
                sub_packets.append(self.__read_packet())
        else:
            sub_packets_number = self.__read_new_binary_number(11)
            for index in range(sub_packets_number):
                if index == 49 and top_level:
                    print()
                sub_packets.append(self.__read_packet())

        match packet_type_id:
            case 0:
                return sum(sub_packets)
            case 1:
                result = sub_packets[0]
                for value in sub_packets[1:]:
                    result *= value
                return result
            case 2:
                return min(sub_packets)
            case 3:
                return max(sub_packets)
            case 5:
                return int(sub_packets[0] > sub_packets[1])
            case 6:
                return int(sub_packets[0] < sub_packets[1])
            case 7:
                return int(sub_packets[0] == sub_packets[1])
            case _:        
                raise ValueError

    def __read_new_binary_number(self, binary_length, as_int=True):
        result = ""
        for _ in range(binary_length):
            result += self.__binary_string[self.__index]
            self.__index += 1
        if as_int:
            result = int(result, 2)
        return result



data = read_data_as_numbers(16, 16, True)
binary_string = "".join(["{0:04b}".format(number) for number in data])
transmission = Transmission(binary_string)

print(sum(transmission.packet_versions))
print(transmission.final_value)
