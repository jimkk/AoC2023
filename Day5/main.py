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

# Part 2

def create_sets(a,b):
    # b in a
    if a[0] < b[1] and a[0] + a[1] > b[1] + b[2]:
        return [
            (a[0], b[1] - a[0]),
            (b[0], b[2]),
            (b[1] + b[2], (a[0] + a[1]) - (b[1] + b[2]))
        ]
    # a in b
    elif a[0] > b[1] and a[0] + a[1] < b[1] + b[2]:
        return [((b[0] - b[1] + a[0]), a[1] )]
    # lower overlap
    elif a[0] > b[1] and a[0] < b[1] + b[2]:
        return [
                (a[0] + (b[0] - b[1]), (b[1] + b[2]) - a[0]),
                (b[1] + b[2], a[0] + a[1] - 1)
            ]
    # higher overlap
    elif b[1] < a[0] + a[1] and a[0] + a[1] < b[1] + b[2]:
        return [
                (a[0], b[1] - a[0]),
                (b[0], a[0] + a[1] - b[1])
            ]
    # no overlap
    else:
        return [a]
    
numbers = [int(x) for x in in_data[0].split(':')[1].strip().split(' ')]
number_sets = [(numbers[x], numbers[x+1]) for x, _ in enumerate(numbers) if x % 2 == 0]

for step in steps:
    for s in step:
        for i, n in enumerate(number_sets):
            new_set = create_sets(n, s)
            number_sets = sum([number_sets[0:i], new_set, number_sets[i+1:]], [])
            if len(new_set) > 1:
                break

x = [x[0] for x in number_sets if x[0] > 0]
x = sorted(x)

print("Part 2: ", x[0])