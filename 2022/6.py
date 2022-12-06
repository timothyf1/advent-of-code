with open("input-files/day6.txt") as f:
    data = f.read()

inp = data.split("\n")[0]

# Part 1
# Note that this only worked by chance
found_letters = []
for index in range(len(inp)):
    if inp[index] in found_letters:
        found_letters = [inp[index]]
        continue
    found_letters.append(inp[index])
    if len(found_letters) == 4:
        print(index+1)
        break

# Part 2
found_letters = []
for index in range(0, len(inp)):
    if inp[index] in found_letters:
        found_letters = found_letters[found_letters.index(inp[index])+1:] + [inp[index]]
        continue
    found_letters.append(inp[index])
    if len(found_letters) == 14:
        print(index+1)
        break