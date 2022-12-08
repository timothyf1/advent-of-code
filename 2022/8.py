with open("input-files/day8.txt") as f:
    data = f.read()

inp = data.split("\n")[:-1]
inp = [[j for j in i] for i in inp]

trn = [list(x) for x in zip(*inp)]

def check_visable(row, col):
    # if len(inp[row][:col]) == 0 or len(inp[row][col+1:]) == 0:
    #     return False

    def check_row():
        if inp[row][col] > max(inp[row][:col]): 
            return True
        if inp[row][col] > max(inp[row][col+1:]):
            return True
        return False

    def check_col():
        if trn[col][row] > max(trn[col][:row]): 
            return True
        if trn[col][row] > max(trn[col][row+1:]):
            return True
        return False

    if check_row() or check_col():
        return True
    return False

def viewing_score(row, col):
    tree_height = inp[row][col]
    west = 1
    for i in range(col-1, 0, -1):
        if inp[row][i] >= tree_height:
            break
        west += 1
    east = 1
    for i in range(col+1, len(inp[row])-1, 1):
        if inp[row][i] >= tree_height:
            break
        east += 1

    north = 1
    for j in range(row-1, 0, -1):
        if trn[col][j] >= tree_height:
            break
        north += 1
    south = 1
    for j in range(row+1, len(trn[col])-1, 1):
        if trn[col][j] >= tree_height:
            break
        south += 1
    return west * east * north * south

num_of_cols = len(inp[0])
num_of_rows = len(inp)
extrenal_vis = num_of_cols * 2 + (num_of_rows-2) * 2

internal_vis = 0
view_scores = {}
for row in range(1, len(inp)-1):
    for col in range(1, len(inp)-1):
        if check_visable(row, col):
            internal_vis += 1
        view_scores[(row, col)] = viewing_score(row, col)
        
print(extrenal_vis+internal_vis)

print(max(view_scores.values()))