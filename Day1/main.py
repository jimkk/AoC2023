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

def min_number(line, word, num):
    min = 1000
    min_word = line.find(word)
    if min_word >= 0:
        min = min_word
    min_num = line.find(num)
    if min_num >= 0 and min_num < min:
        min = min_num
    return min

def max_number(line, word, num):
    max = -1
    max_word = line.rfind(word)
    if max_word >= 0:
        max = max_word
    max_num = line.rfind(num)
    if max_num >= 0 and max_num > max:
        max = max_num
    return max

total = 0
for line in in_data:
    indexes = []
    for word, num in string_to_num_dict.items():
        indexes.append([])
        indexes[num-1].append(min_number(line, word, str(num)) if min_number(line, word, str(num))  < 1000 else None)
        indexes[num-1].append(max_number(line, word, str(num)) if max_number(line, word, str(num)) > -1 else None)
    first_number = [[x+1, indexes[x][0]] for x in range(len(indexes))]
    what = [x for x in first_number if x[1] is not None]
    first_number = sorted([x for x in first_number if x[1] is not None], key=lambda x: x[1])[0][0]
    last_number = [[x+1, indexes[x][1]] for x in range(len(indexes))]
    last_number = sorted([x for x in last_number if x[1] is not None], key=lambda x: x[1], reverse=True)[0][0]
    line_value = int(str(first_number) + str(last_number))

    total += line_value

print("Part 2: ", total)