def find(location):
    # Find a specfic value on the height map (for S and E)
    for i in range(len(data[0])):
        for j in range(len(data)):
            if location == data[j][i]:
                return (i, j)

def pos_move(pos):
    # Returns a list of possible moves from the given location
    x, y = pos
    pos_moves = []
    if x > 0 and data_num[y][x-1] - data_num[y][x] <= 1:
        pos_moves.append('left')
    if x < len(data_num[y])-1:
        if data_num[y][x+1] - data_num[y][x] <= 1:
            pos_moves.append('right')
    if y > 0 and data_num[y-1][x] - data_num[y][x] <= 1:
        pos_moves.append('up')
    if y < len(data_num)-1:
        if data_num[y+1][x] - data_num[y][x] <=1:
            pos_moves.append('down')
    return pos_moves

def move_pos(pos, direction):
    # Returns the new location coordinates from a given move and position
    x, y = pos
    if direction == 'left':
        x_move = x - 1
        y_move = y
    if direction == 'right':
        x_move = x + 1
        y_move = y
    if direction == 'up':
        x_move = x
        y_move = y - 1
    if direction == 'down':
        x_move = x
        y_move = y + 1
    return (x_move, y_move)

def find_a():
    # Find the location of all a's returned as a set
    locations = set()
    for i in range(len(data[0])):
        for j in range(len(data)):
            if 'a' == data[j][i]:
                locations.add((i, j))
    return locations

def find_shortest_path_length(start, end):
    current_step_locations = start
    steps_from_start = {}
    count = 0

    while len(current_step_locations) > 0:
        next_locations = set()
        for location in current_step_locations:
            # Saving how many steps to get to this location
            steps_from_start[location] = count

            # Finding what moves are possible from current location
            pos_moves = pos_move(location)

            for move in pos_moves:
                move_location = move_pos(location, move)

                # Checking to see we haven't already visited the next location
                if move_location not in steps_from_start:
                    next_locations.add(move_location)

        # Setting the next set of new locations reached
        current_step_locations = next_locations

        count += 1

    return steps_from_start[end]

with open('input-files/day12.txt') as f:
    data = f.read()

data = [list(i) for i in data.split('\n')[:-1]]

heights = {
    "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7,
    "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14,
    "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20,
    "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26,
    "S" : 1, "E" : 26
}

data_num = [[heights[j] for j in i] for i in data]


start = set([find("S")])
end = find("E")
print(find_shortest_path_length(start, end))

location_of_a = find_a()
print(find_shortest_path_length(location_of_a, end))