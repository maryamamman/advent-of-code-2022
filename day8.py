def is_visible(tree, right, left, top, down):
    if(max(right)<tree or max(left)<tree or \
        max(down)<tree or max(top)<tree):
            return 1
    return 0

def find_scenic_score(tree, right, left, top, down):
    right_view_dist = 0
    left_view_dist = 0
    down_view_dist = 0
    top_view_dist = 0
    for x in range(0, len(right)):
        if right[x] >= tree:
            right_view_dist = x + 1
            break
        else:
            right_view_dist = len(right)
    for x in range(len(left)- 1, 0, -1):
        if left[x] >= tree:
            left_view_dist = len(left) - x - 1
            break
        else:
            left_view_dist = len(left)
    for x in range(0, len(down)):
        if down[x] >= tree:
            down_view_dist = x + 1
            break
        else:
            down_view_dist = len(down)
    for x in range(len(top)- 1, 0, -1):
        if top[x] >= tree:
            top_view_dist = len(top) - x - 1
            break
        else:
            top_view_dist = len(top)
            
    scenic_score = right_view_dist * left_view_dist * down_view_dist * top_view_dist
    return scenic_score


with open("input.txt") as file:
    trees = file.readlines()


x_max = len(trees[0]) - 1
y_max = len(trees)
visible_trees = 2 * x_max + 2 * y_max - 4
scenic_scores = []


for i in range(1,y_max-1):
    for j in range(1,x_max-1):
        tree = int(trees[i][j])
        left = [int(x) for x in list(trees[i][0:j])]
        right = [int(x) for x in list(trees[i][j+1:x_max])]
        down = [int(trees[x][j]) for x in range(i+1, y_max)]
        top = [int(trees[x][j]) for x in range(0, i)]
        
        visible_trees += is_visible(tree, right, left, top, down)
        scenic_scores.append(find_scenic_score(tree, right, left, top, down))
        
print(f"Part 1: {visible_trees}\nPart 2: {max(scenic_scores)}")