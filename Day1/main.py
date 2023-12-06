import re

# Part 1
with open('Day1/input.txt', 'r', encoding='UTF-8') as f:
    in_data = f.readlines()
    in_data = [x.strip() for x in in_data]

total = 0
for line in in_data:
    re_result = re.findall(r'\d', line)
    line_value = int(re_result[0] + re_result[-1])
    total += line_value

print("Part 1: ", total)

# Part 2
with open('Day1/input.txt', 'r', encoding='UTF-8') as f:
    in_data = f.readlines()
    in_data = [x.strip() for x in in_data]

string_to_num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
for num in range(0,10):
    string_to_num_dict[str(num)] = num

total = 0
for line in in_data:
    indexes = []
    for key, value in string_to_num_dict.items():
        matches = re.finditer(key, line)
        for m in matches:
            indexes.append([value, m.start()])
    first_number = sorted([x for x in indexes], key=lambda x: x[1])[0][0]
    last_number = sorted([x for x in indexes], key=lambda x: x[1], reverse=True)[0][0]
    line_value = int(str(first_number) + str(last_number))

    total += line_value

print("Part 2: ", total)