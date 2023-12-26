with open('Day5/input.txt', 'r', encoding='utf8') as f:
    in_data = f.read()

in_data = [x.strip() for x in in_data.split('\n\n')]

numbers = [int(x) for x in in_data[0].split(':')[1].strip().split(' ')]
steps = [[[int(z) for z in y.split(' ')] for y in x.split(':')[1].strip().split('\n')] for x in in_data[1:]]

for step in steps:
    for i, num in enumerate(numbers):
        for group in step:
            if num in range(group[1], group[1] + group[2]):
                numbers[i] = num + (group[0] - group[1])

print('Part 1: ', min(numbers))