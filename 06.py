from Utils import read_data_as_numbers

def number_of_fishes(initial_fishes, days):
    fishes_by_timer_value = [0] * (1 + 8)
    for timer_value in initial_fishes:
        fishes_by_timer_value[timer_value] += 1
    
    for _ in range(days):
        fishes_with_zero_timer = fishes_by_timer_value[0]
        for timer_value in range(1, len(fishes_by_timer_value)):
            fishes_by_timer_value[timer_value - 1] = fishes_by_timer_value[timer_value]
        fishes_by_timer_value[6] += fishes_with_zero_timer
        fishes_by_timer_value[8] = fishes_with_zero_timer

    return sum(fishes_by_timer_value)

initial_fishes = read_data_as_numbers(6)
print(number_of_fishes(initial_fishes, 80))
print(number_of_fishes(initial_fishes, 256))
