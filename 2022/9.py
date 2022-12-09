with open("input-files/day9.txt") as f:
    data = f.read()

inp = data.split("\n")[:-1]
moves = [i.split(" ") for i in inp]
head = [0,0]
tail = [0,0]
tail_2_1 = [0,0]
tail_2_2 = [0,0]
tail_2_3 = [0,0]
tail_2_4 = [0,0]
tail_2_5 = [0,0]
tail_2_6 = [0,0]
tail_2_7 = [0,0]
tail_2_8 = [0,0]
tail_2_9 = [0,0]

tail_visited = set([(0, 0)])
tail_visited_2 = set([(0, 0)])

def tail_adjacent(head, tail):
    if abs(head[0]-tail[0]) > 1:
        return False
    if abs(head[1]-tail[1]) > 1:
        return False
    return True

def move_tail(head, tail):
    if (abs(head[0]-tail[0]) >= 1 and abs(head[1]-tail[1]) > 1) or (abs(head[0]-tail[0]) > 1 and abs(head[1]-tail[1]) >= 1):
        if head[0]-tail[0] >= 1 and head[1]-tail[1] >= 1:
            # print("RU")
            tail[0] += 1
            tail[1] += 1
        elif head[0]-tail[0] <= -1 and head[1]-tail[1] >= 1:
            # print("LU")
            tail[0] -= 1
            tail[1] += 1
        elif head[0]-tail[0] <= -1 and head[1]-tail[1] <= -1:
            # print("LD")
            tail[0] -= 1
            tail[1] -= 1
        elif head[0]-tail[0] >= 1 and head[1]-tail[1] <= -1:
            # print("RD")
            tail[0] += 1
            tail[1] -= 1

    elif abs(head[0]-tail[0]) > 1:
        if head[0]-tail[0] > 0:
            # print("x r")
            tail[0] += 1
        else:
            # print("x l")
            tail[0] -= 1
    elif abs(head[1]-tail[1]) > 1:
        if head[1]-tail[1] > 0:
            tail[1] += 1
        else:
            tail[1] -= 1
    return tail

for move in moves:
    for j in range(int(move[1])):
        if move[0] == "U":
            head[1] += 1
        if move[0] == "D":
            head[1] -= 1
        if move[0] == "R":
            head[0] += 1
        if move[0] == "L":
            head[0] -= 1
        # print(head, tail, f"[{head[0]-tail[0]}, {head[1]-tail[1]}]", abs(head[0]-tail[0])+abs(head[1]-tail[1]))
        if not tail_adjacent(head, tail):
            tail = move_tail(head, tail)
        if not tail_adjacent(head, tail_2_1):
            tail_2_1 = move_tail(head, tail_2_1)
        if not tail_adjacent(tail_2_1, tail_2_2):
            tail_2_2 = move_tail(tail_2_1, tail_2_2)
        if not tail_adjacent(tail_2_2, tail_2_3):
            tail_2_3 = move_tail(tail_2_2, tail_2_3)
        if not tail_adjacent(tail_2_3, tail_2_4):
            tail_2_4 = move_tail(tail_2_3, tail_2_4)
        if not tail_adjacent(tail_2_4, tail_2_5):
            tail_2_5 = move_tail(tail_2_4, tail_2_5)
        if not tail_adjacent(tail_2_5, tail_2_6):
            tail_2_6 = move_tail(tail_2_5, tail_2_6)
        if not tail_adjacent(tail_2_6, tail_2_7):
            tail_2_7 = move_tail(tail_2_6, tail_2_7)
        if not tail_adjacent(tail_2_7, tail_2_8):
            tail_2_8 = move_tail(tail_2_7, tail_2_8)
        if not tail_adjacent(tail_2_8, tail_2_9):
            tail_2_9 = move_tail(tail_2_8, tail_2_9)

        tail_visited.add(tuple(tail))
        tail_visited_2.add(tuple(tail_2_9))

# print(tail_visited)
print(len(tail_visited))
print(len(tail_visited_2))
