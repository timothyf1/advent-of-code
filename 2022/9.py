with open("input-files/day9.txt") as f:
    data = f.read()

inp = data.split("\n")[:-1]
moves = [i.split(" ") for i in inp]

snake = [[0, 0] for i in range(10)]

tail_visited_1 = set([(0, 0)])
tail_visited_2 = set([(0, 0)])

def move_head(head, move):
    if move == "U":
        head[1] += 1
    elif move == "D":
        head[1] -= 1
    elif move == "R":
        head[0] += 1
    elif move == "L":
        head[0] -= 1
    return head

def tail_adjacent(head, tail):
    if abs(head[0]-tail[0]) > 1:
        return False
    if abs(head[1]-tail[1]) > 1:
        return False
    return True

def move_tail(head, tail):
    if abs(head[0]-tail[0]) + abs(head[1]-tail[1]) > 2:
        if head[0]-tail[0] >= 1 and head[1]-tail[1] >= 1:
            tail[0] += 1
            tail[1] += 1
        elif head[0]-tail[0] <= -1 and head[1]-tail[1] >= 1:
            tail[0] -= 1
            tail[1] += 1
        elif head[0]-tail[0] <= -1 and head[1]-tail[1] <= -1:
            tail[0] -= 1
            tail[1] -= 1
        elif head[0]-tail[0] >= 1 and head[1]-tail[1] <= -1:
            tail[0] += 1
            tail[1] -= 1

    elif abs(head[0]-tail[0]) > 1:
        if head[0]-tail[0] > 0:
            tail[0] += 1
        else:
            tail[0] -= 1
    elif abs(head[1]-tail[1]) > 1:
        if head[1]-tail[1] > 0:
            tail[1] += 1
        else:
            tail[1] -= 1
    return tail

for move in moves:
    for j in range(int(move[1])):
        snake[0] = move_head(snake[0], move[0])

        for i in range(1, len(snake)):
            if tail_adjacent(snake[i-1], snake[i]):
                break
            snake[i] = move_tail(snake[i-1], snake[i])

        tail_visited_1.add(tuple(snake[1]))
        tail_visited_2.add(tuple(snake[-1]))

print(len(tail_visited_1))
print(len(tail_visited_2))
