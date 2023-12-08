import re

with open('Day4/input.txt', 'r', encoding='UTF-8') as f:
    in_data = f.read()
in_data = [x.strip() for x in in_data.split('\n')]

# Part 1

games = []
copies = [1 for x in in_data]
for i, game in enumerate(in_data):
    game_parts = game.split(': ')
    game_id = int(re.search(r'\d+', game_parts[0]).group())
    game_numbers = game_parts[1].split(' | ')
    winning_numbers = [int(x) for x in re.findall(r'\d+', game_numbers[0])]
    player_numbers = [int(x) for x in re.findall(r'\d+', game_numbers[1])]
    game = [game_id, winning_numbers, player_numbers]
    points = 0
    winners = [x for x in game[1] if x in game[2]]
    if len(winners) > 0:
        points = 2 ** (len(winners) - 1)
        for j in range(i + 1, i + len(winners) + 1):
            copies[j] = copies[j] + 1 * copies[i]
    game.append(points)
    games.append(game)


total_points = sum([x[3] for x in games])
print('Part 1: ', total_points)

# Part 2

total_cards = sum(copies)
print('Part 1: ', total_cards)
