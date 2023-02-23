class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []
    
home = Dir("home", None)
dirs = [home]
current_dir = home

with open("input.txt") as file:
    command_lines = file.readlines()
    
commands = []
for line in command_lines:
    commands.append(line.split())

for command in commands:
    
    if command[0] == "$":
        
        if command[1] == "ls":
            pass
        
        elif command[1] == "cd":
            
            if command[2] == "/":
                current_dir = home

            elif command[2] == "..":
                current_dir = current_dir.parent

            else:
                dir_name = command[2]
                for dir in current_dir.children:
                    if dir.name == dir_name:
                        current_dir = dir
                        break

    elif command[0] == "dir":
        dir_name = command[1]
        new_dir = Dir(dir_name, current_dir)
        current_dir.children.append(new_dir)
        dirs.append(new_dir)
        
    else:
        size = int(command[0])
        temp = current_dir
        while current_dir != None:
            current_dir.size += size
            current_dir = current_dir.parent
        current_dir = temp
    

total = 0

used_space = home.size
limit = 30000000 - (70000000 - used_space)
deletable = [] #😐

for dir in dirs:
    if dir.size < 100000:
        total += dir.size

    if limit <= dir.size:
        deletable.append(dir.size)

minimum = min(deletable)

print(f"Part 1: {total}\nPart 2: {minimum}")