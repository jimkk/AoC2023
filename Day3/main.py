import re
from itertools import product

with open('Day3/input.txt', 'r', encoding='UTF-8') as f:
    in_data = f.read()
    in_data = [x.strip() for x in in_data.split('\n')]

def find_symbols(in_array):
    symbols = []
    for i, line in enumerate(in_array):
        matches = re.finditer(r'[^\d\.]', line)
        for match in matches:
            symbols.append([i, match.start()])
    return symbols

def find_numbers(in_array):
    numbers = []
    for i, line in enumerate(in_array):
        matches = re.finditer(r'\d+', line)
        for match in matches:
            number_data = [int(match.group()), [[i,match.start()], [i,match.end()-1]]]
            x_range = [*range(number_data[1][0][0]-1, number_data[1][1][0]+2)]
            y_range = [*range(number_data[1][0][1]-1, number_data[1][1][1]+2)]
            locations_to_check = [[x,y] for x,y in product(x_range, y_range)]
            number_data.append(locations_to_check)
            numbers.append(number_data)
    return numbers

def check_surroundings(locations, symbols):
    for possible_symbol_locations in locations:
        if possible_symbol_locations in symbols:
            return True
    return False


symbol_locations = find_symbols(in_data)
number_locations = find_numbers(in_data)
total = 0
for number in number_locations:
    if check_surroundings(number[2], symbol_locations):
        total += number[0]


print('Part 1: ', total)

# Part 2

def find_gears(in_array):
    symbols = []
    for i, line in enumerate(in_array):
        matches = re.finditer(r'[\*]', line)
        for match in matches:
            symbols.append([i, match.start()])
    return symbols

def surrounding_numbers(gear, number_locations):
    numbers = []
    for i, number in enumerate(number_locations):
        if i not in [x[0] for x in numbers] and gear in number[2]:
            numbers.append([i,number[0]])
    return [x[1] for x in numbers]

total = 0
for gear in find_gears(in_data):
    nums = surrounding_numbers(gear, number_locations)
    if len(nums) == 2:
        total += nums[0] * nums[1]

print('Part 2: ', total)