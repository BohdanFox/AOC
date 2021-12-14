from collections import defaultdict
from Utils import read_data

STEPS = 40

unparsed_data = read_data(14)
original_string = unparsed_data[0]
rules = dict([entry.split(" -> ") for entry in unparsed_data[2:]])

symbol_pair_counts = defaultdict(int)
for i in range(1, len(original_string)):
    symbol_pair_counts[original_string[i - 1] + original_string[i]] += 1

for step in range(STEPS):
    new_symbol_pairs_counts = defaultdict(int)
    for symbol_pair, value in symbol_pair_counts.items():
        new_symbol = rules[symbol_pair]
        new_symbol_pairs_counts[symbol_pair[0] + new_symbol] += value
        new_symbol_pairs_counts[new_symbol + symbol_pair[1]] += value
    symbol_pair_counts = new_symbol_pairs_counts

symbol_count = defaultdict(int)
for symbol_pair, value in symbol_pair_counts.items():
    symbol_count[symbol_pair[0]] += value / 2
    symbol_count[symbol_pair[1]] += value / 2
symbol_count[original_string[0]] += 1 / 2
symbol_count[original_string[-1]] += 1 / 2

result = max(symbol_count.values()) - min(symbol_count.values())
print(int(result))
