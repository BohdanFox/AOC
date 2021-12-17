import re
from typing import Tuple
import numpy as np
from Utils import read_data


class Target:
    def __init__(self, x1, x2, y1, y2) -> None:
        self.min_x = min(int(x1), int(x2))
        self.max_x = max(int(x1), int(x2))
        self.min_y = min(int(y1), int(y2))
        self.max_y = max(int(y1), int(y2))


def shoot(x_velocity: int, y_veloicty: int, target: Target) -> Tuple[bool, int]:
    x, y = 0, 0
    max_height = y
    falling = False
    while not (y < target.min_y and falling):
        x += x_velocity
        y += y_veloicty
        x_velocity -= np.sign(x_velocity)
        y_veloicty -= 1
        falling = y_veloicty < 0
        max_height = max(y, max_height)
        if target.min_x <= x <= target.max_x and target.min_y <= y <= target.max_y:
            return True, max_height
    return False, max_height


raw_data = read_data(17)[0]
(x1, x2, y1, y2) = re.findall(r"=(-?\d+)..(-?\d+).*=(-?\d+)..(-?\d+)", raw_data)[0]
target = Target(x1, x2, y1, y2)

sucessful_shoots = []
for y in range(target.min_y, target.max_x + 1):
    for x in range(target.max_x + 1):
        has_reached_target, max_height = shoot(x, y, target)
        if has_reached_target:
            sucessful_shoots.append([x, y, max_height])

print(len(sucessful_shoots))
print(max(np.array(sucessful_shoots)[:, 2]))
