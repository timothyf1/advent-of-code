with open('input-files/day14.txt') as f:
    data = f.read()

data = [i.split(' -> ') for i in data.split('\n')[:-1]]

data = [[tuple(j.split(',')) for j in i] for i in data]
data = [[(int(j[0]), int(j[1])) for j in i] for i in data]

class grid():

    def __init__(self, inp):
        self.left = min([j[0] for i in data for j in i])
        self.right = max([j[0] for i in data for j in i])
        self.top = 0
        self.bottom = max([j[1] for i in data for j in i])
        self.grid = [['.' for j in range(self.left, self.right+1)] for i in range(self.bottom+1)]

    def print_grid(self):
        for row in self.grid:
            print(''.join(row))

    def add_line(self, inp):
        inp = [(i[0]-self.left, i[1]) for i in inp]
        for i in range(len(inp)-1):
            if inp[i][0] == inp[i+1][0]:
                col = inp[i][0]
                rows_index = [inp[i][1], inp[i+1][1]]
                rows_index.sort()
                for row in range(rows_index[0], rows_index[1]+1):
                    self.grid[row][col] = '#'
            if inp[i][1] == inp[i+1][1]:
                row = inp[i][1]
                cols_index = [inp[i][0], inp[i+1][0]]
                cols_index.sort()
                for col in range(cols_index[0], cols_index[1]+1):
                    self.grid[row][col] = '#'

    def sand_drop(self):
        sand_moving = True
        sand_pos = (500-self.left, 0)
        try:
            while sand_moving:
                # Down
                if self.grid[sand_pos[1]+1][sand_pos[0]] == '.':
                    self.grid[sand_pos[1]][sand_pos[0]] = '.'
                    self.grid[sand_pos[1]+1][sand_pos[0]] = 'O'
                    sand_pos = (sand_pos[0], sand_pos[1]+1)

                # Down left
                elif self.grid[sand_pos[1]+1][sand_pos[0]-1] == '.':
                    self.grid[sand_pos[1]][sand_pos[0]] = '.'
                    self.grid[sand_pos[1]+1][sand_pos[0]-1] = 'O'
                    sand_pos = (sand_pos[0]-1, sand_pos[1]+1)

                # Down right
                elif self.grid[sand_pos[1]+1][sand_pos[0]+1] == '.':
                    self.grid[sand_pos[1]][sand_pos[0]] = '.'
                    self.grid[sand_pos[1]+1][sand_pos[0]+1] = 'O'
                    sand_pos = (sand_pos[0]+1, sand_pos[1]+1)

                else:
                    sand_moving = False
        except:
            return False
        return True

alpha = grid(data)
for line in data:
    alpha.add_line(line)

count = 0
while alpha.sand_drop():
    print(count)
    # alpha.print_grid()
    count += 1

print(count)

with open('out.txt', 'w') as f:
    out = '\n'.join([''.join(i) for i in alpha.grid])
    f.writelines(out)