from copy import copy
import math
with open('sample/day12.txt') as f:
    data = f.read()

data = data.split('\n')[:-1]
data = [list(i) for i in data]

heights = {
    "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7,
    "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14,
    "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20,
    "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26,
    "S" : 1, "E" : 27
}

inp = [[heights[j] for j in i] for i in data]

def find(location):
    for i in range(len(data[0])):
        for j in range(len(data)):
            if location == data[j][i]:
                return (i, j)

def move(x, y, visited = set()):
    # print(x, y)
    visit_local = copy(visited)
    visit_local.add((x, y))
    if (x, y) in cache:
        # print('cache')
        return cache[(x, y)]
    if inp[y][x] == 27:
        return 0

    # Allowed directions
    pos_moves = []
    if x > 0 and -1 <= inp[y][x-1] - inp[y][x] <= 1:
        pos_moves.append('left')
    if x < len(inp[y])-1:
        if -3 <= inp[y][x+1] - inp[y][x] <= 1:
            pos_moves.append('right')
    if y > 0 and -1 <= inp[y-1][x] - inp[y][x] <= 1:
        pos_moves.append('up')
    if y < len(inp)-1:
        if -3 <= inp[y+1][x] - inp[y][x] <=1:
            pos_moves.append('down')
    # print(pos_moves)
    move_dist = []
    for move_dir in pos_moves:
        if move_dir == 'left':
            x_move = x - 1
            y_move = y
        if move_dir == 'right':
            x_move = x + 1
            y_move = y
        if move_dir == 'up':
            x_move = x
            y_move = y - 1
        if move_dir == 'down':
            x_move = x
            y_move = y + 1
        # print(move_dir, x_move, y_move)
        if (x_move, y_move) not in visit_local:
            visit_local.add((x_move, y_move))
            move_dist.append(move(x_move, y_move, visit_local)+1)
        #     print("back to last location")
        # else:
        #     print("visited")

    # print(move_dist)
    if len(move_dist) != 0:
        if (x, y) in cache:
            min(cache[(x, y)], min(move_dist))
            cache[(x, y)] = min(cache[(x, y)], min(move_dist))
        else:
            cache[(x, y)] = min(move_dist)
        return cache[(x, y)]
    return math.inf

start_x, start_y = find("S")
cache = {}
print(move(start_x, start_y))