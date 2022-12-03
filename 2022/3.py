with open("input-files/day3.txt") as f:
    data = f.read()

inp = data.split("\n")[:-1]

priorities = {
    "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, 
    "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, 
    "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, 
    "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26,
    "A" : 27, "B" : 28, "C" : 29, "D" : 30, "E" : 31, "F" : 32, "G" : 33,
    "H" : 34, "I" : 35, "J" : 36, "K" : 37, "L" : 38, "M" : 39, "N" : 40,
    "O" : 41, "P" : 42, "Q" : 43, "R" : 44, "S" : 45, "T" : 46,
    "U" : 47, "V" : 48, "W" : 49, "X" : 50, "Y" : 51, "Z" : 52,
}

def common_letter_bag_half(l):
    return list(set(l[0]).intersection(set(l[1])))[0]

inp_elf = [[i[:len(i)//2], i[len(i)//2:]] for i in inp]
common_letters = [common_letter_bag_half(i) for i in inp_elf]
priority = [priorities[i] for i in common_letters]

print(sum(priority))

def badge(l):
    return list(set(l[0]).intersection(set(l[1]).intersection(set(l[2]))))[0]

groups_bags = [[inp[i], inp[i+1], inp[i+2]] for i in range(0, len(inp), 3)]
group_badges = [badge(i) for i in groups_bags]
group_priority = [priorities[i] for i in group_badges]

print(sum(group_priority))


