import copy

with open("input-files/aoc_2022_day05_large_input.txt") as f:
    data = f.read()

data = data.split("\n\n")

stacks_data = data[0].split("\n")
moves = [i.split(" ") for i in data[1].split("\n")][:-1]
moves = [[int(i) for i in j if i.isdigit()] for j in moves]

num_of_stacks = len([i for i in stacks_data.pop().split(" ") if i != ""])

stacks = [[] for i in range(num_of_stacks)]

for i in range(len(stacks_data)-1, -1, -1):
    for j in range(num_of_stacks):
        if stacks_data[i][j*4+1] != " ":
            stacks[j].append(stacks_data[i][j*4+1]) 

stacks_two = copy.deepcopy(stacks)

for move in moves:
    for i in range(move[0]):
        stacks[move[2]-1].append(stacks[move[1]-1].pop())

top_crates= "".join([i[-1] for i in stacks])

print(top_crates)

# for move in moves:
#     stacks_two[move[2]-1] += stacks_two[move[1]-1][-move[0]:]
#     stacks_two[move[1]-1] = stacks_two[move[1]-1][:-move[0]]


# top_crates_2 = "".join([i[-1] for i in stacks_two])

# print(top_crates_2)
