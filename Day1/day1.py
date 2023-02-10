with open('input.txt', 'r') as inp:
    calories = [[int(calorie) for calorie in elf.split("\n")] for elf in inp.read()[:-1].split("\n\n")]

top = max(sum(x) for x in calories)
top_three = sum(sorted([sum(x) for x in calories])[-3:])

print(f"Part 1: {top}\nPart 2: {top_three}")
