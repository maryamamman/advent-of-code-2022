with open('input.txt', 'r') as inp:
    rucksacks = inp.read().splitlines()

priority = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def find_common(comp1, comp2):
    for item in comp1:
        if item in comp2:
            return item


def find_badge(ruck1, ruck2, ruck3):
    for item in ruck1:
        if item in ruck2 and item in ruck3:
            return item


def find_priority(item):
    for i in range(26):
        if item == priority[i]:
            return i + 1
        if item.lower() == priority[i]:
            return i + 1 + len(priority)


sum_common = 0
for rucksack in rucksacks:
    compartment_len = len(rucksack) // 2
    first_compartment = rucksack[0:compartment_len]
    second_compartment = rucksack[compartment_len:]

    common_item = find_common(first_compartment, second_compartment)
    sum_common += find_priority(common_item)


sum_badge = 0
for i in range(0, len(rucksacks), 3):
    rucksack1 = rucksacks[i]
    rucksack2 = rucksacks[i + 1]
    rucksack3 = rucksacks[i + 2]

    badge_item = find_badge(rucksack1, rucksack2, rucksack3)
    sum_badge += find_priority(badge_item)

print(f"Part 1: {sum_common}\nPart 2: {sum_badge}")
