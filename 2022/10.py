with open('input-files/day10.txt') as f:
    data = f.read()

inp = data.split('\n')[:-1]
inp = [i.split(' ') for i in inp]

cycles = 1
sum_1 = 0
x = 1
display = ['' for i in range(6)]

def display_pixel():
    display[(cycles-1) // 40] += '#' if (cycles-1) % 40 in [x-1, x, x+1] else ' '

for line in inp:
    if cycles in [20, 60, 100, 140, 180, 220]:
        sum_1 += x * cycles
    display_pixel()
    if line[0] == 'noop':
        cycles += 1
    else:
        cycles += 1
        if cycles in [20, 60, 100, 140, 180, 220]:
            sum_1 += x * cycles
        display_pixel()
        cycles += 1
        x += int(line[1])

print(sum_1)
print(display[0])
print(display[1])
print(display[2])
print(display[3])
print(display[4])
print(display[5])