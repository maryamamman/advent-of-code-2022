with open('input.txt', 'r') as inp:
    rounds = inp.read().strip().split("\n")

p1_points = {
    "A X": 4, "B X": 1, "C X": 7,
    "A Y": 8, "B Y": 5, "C Y": 2,
    "A Z": 3, "B Z": 9, "C Z": 6
}

p2_points = {
    "A X": 3, "B X": 1, "C X": 2,
    "A Y": 4, "B Y": 5, "C Y": 6,
    "A Z": 8, "B Z": 9, "C Z": 7
}

p1_scores = 0
for rnd in rounds:
    p1_scores += p1_points[rnd]

p2_scores = 0
for rnd in rounds:
    p2_scores += p2_points[rnd]

print(f"Part 1: {p1_scores}\nPart 2: {p2_scores}")
