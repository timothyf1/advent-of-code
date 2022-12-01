with open("input-files/day1.txt") as f:
    data = f.read()

elf_list = data[:-1].split("\n\n")
elf_list = [elem.split("\n") for elem in elf_list]
elf_list = [[int(i) for i in j] for j in elf_list]

elf_cal = [sum(i) for i in elf_list]

print(max(elf_cal))

elf_cal.sort()

top3 = [elf_cal[-1], elf_cal[-2], elf_cal[-3]]
print(sum(top3))