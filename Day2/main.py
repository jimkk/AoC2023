from functools import reduce

with open('Day2/input.txt', 'r', encoding='UTF-8') as f:
    in_data = f.read().split('\n')

class Game:
    id = 0
    rounds = []
    def __init__(self, id, rounds):
        self.id = id
        self.rounds = rounds

    def check_valid(self, max_red, max_green, max_blue):
        for round in self.rounds:
            if not round.check_valid(max_red, max_green, max_blue):
                return False
        return True
    
    def min_cubes(self):
        min_reds = max([round.cubes[0] for round in self.rounds])
        min_greens = max([round.cubes[1] for round in self.rounds])
        min_blues = max([round.cubes[2] for round in self.rounds])
        return [min_reds, min_greens, min_blues]

class Round:
    cubes = []

    def __init__(self, round_str):
        round_parts = round_str.split(', ')
        reds = sum([int(x.split(' ')[0]) for x in round_parts if x.endswith('red')])
        greens = sum([int(x.split(' ')[0]) for x in round_parts if x.endswith('green')])
        blues = sum([int(x.split(' ')[0]) for x in round_parts if x.endswith('blue')])
        self.cubes = [reds, greens, blues]

    def check_valid(self, max_red, max_green, max_blue):
        if self.cubes[0] > max_red:
            return False
        if self.cubes[1] > max_green:
            return False
        if self.cubes[2] > max_blue:
            return False
        return True

games = []
for game in in_data:
    game_sections = game.split(': ')
    games.append(
        Game(
            int(game_sections[0].split(' ')[1]),
            [Round(round) for round in game_sections[1].split('; ')]
        )
    )

valid_ids = [g.id for g in games if g.check_valid(12,13,14)]
print('Part 1: ', sum(valid_ids))

# Part 2
cube_powers = [reduce(lambda x,y: x*y, game.min_cubes()) for game in games]
print('Part 2: ', sum(cube_powers))