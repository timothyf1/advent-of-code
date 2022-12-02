with open("input-files/day2.txt") as f:

    data = f.read()


inp = data.split("\n")

inp = [i.split(" ") for i in inp][:-1]


# A = Rock, B = Paper, C = Scissors

# X = Rock, Y = Paper, Z = Scissors


score = 0
new_score = 0

for line in inp:
    
    if line[1] == "X":
        if line[0] == "A":
            score += 4
            new_score += 3
        if line[0] == "B":
            score += 1
            new_score += 1
        if line[0] == "C":
            score += 7
            new_score += 2
    if line[1] == "Y":
        if line[0] == "A":
            score += 8
            new_score += 4
        if line[0] == "B":
            score += 5
            new_score += 5
        if line[0] == "C":
            score += 2
            new_score += 6
    if line[1] == "Z":
        if line[0] == "A":
            score += 3
            new_score += 8
        if line[0] == "B":
            score += 9
            new_score += 9
        if line[0] == "C":
            score += 6
            new_score += 7


print(score)
print(new_score)