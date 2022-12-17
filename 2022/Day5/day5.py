def find_border(input):
    for i in input:
        if i.startswith('move'):
            return input.index(i) - 1
        
def make_stacks(stacks_part):
    cols = []
    for line in stacks_part:
        cols.append([line[i:i+3] for i in range(0, len(line), 4)])
        
    
    stacks = []
    for j in range(9):
        s = []
        for i in cols:
            s.append(i[j])
        stacks.append(s)
    
    
    for i in stacks:
        while '   ' in i:
            i.remove('   ')
            
    return stacks


def part1_rearrangement(org_stacks, rearrangement_procedure):
    stacksq = org_stacks
    for i in rearrangement_procedure:
        number = int(i[5:7])
        from_s = int(i[12:14]) - 1
        to_s = int(i[17:19]) - 1
        for j in range(number):
            stacksq[to_s].append(stacksq[from_s][-1])
            stacksq[from_s].pop(-1)
    
    tops = ''   
    for i in stacksq:
        tops += i[-1][1]
    return tops

def part2_rearrangement(org_stacks, rearrangement_procedure):
    stacks = org_stacks.copy()
    for i in rearrangement_procedure:
        number = int(i[5:7])
        from_s = int(i[12:14]) - 1
        to_s = int(i[17:19]) - 1
        transferring_index = len(stacks[from_s]) - number
        for j in range(number):
            stacks[to_s].append(stacks[from_s][transferring_index])
            stacks[from_s].pop(transferring_index)
        
    tops = ''
    for i in stacks:
        tops += i[-1][1]
    return tops

with open('input.txt', 'r') as inp:
    input = inp.read().splitlines()
    border = find_border(input)
    
    # stacks
    stacks_part = input[0:border - 1]
    stacks_part.reverse()
    
    stacks = make_stacks(stacks_part)
    
    # rearrangement procedure 
    rearrangement_procedure = input[border + 1:]
    
    
    # print(part1_rearrangement(stacks, rearrangement_procedure))
        
    # print(part2_rearrangement(stacks, rearrangement_procedure))