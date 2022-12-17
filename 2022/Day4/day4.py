def one_conrains_other(pair):
    return (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) \
        or (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1])


def overlap(pair):
    return (pair[1][0] <= pair[0][0] <= pair[1][1]) \
        or (pair[0][0] <= pair[1][0] <= pair[0][1])


with open('input.txt', 'r') as inp:
    thefile = inp.read().splitlines()

    pairs = [[[int(i) for i in pair.split("-")] for pair in line.split(",")] for line in thefile]
    
    part1 = 0
    part2 = 0
    
    for pair in pairs:
        if one_conrains_other(pair):
            part1 += 1
        if overlap(pair):
            part2 += 1

    print(f"Part 1: {part1}\nPart 2: {part2}")
