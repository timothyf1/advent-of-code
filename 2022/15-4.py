class grid():

    def __init__(self, data, limit, y):
        self.grid_2 = {}
        self.set_1 = set()
        self.min_x, self.max_x, self.min_y, self.max_y = self.min_max(data)
        self.max_dist = 0
        self.y = y
        self.limit = limit

        for pair in data:
            print(f"Starting pair {pair}")
            # self.add_sensor(pair[0])
            # self.add_beacon(pair[1])
            pair_distance = self.dist(pair[0], pair[1])
            self.max_dist = max(self.max_dist, pair_distance)
            self.pos_within_range_2(pair[0], pair_distance)
            
        print("Finished adding to dict")
        # self.pos_within_range(data[6][0], 9)

    def pos_within_range_2(self, sensor_pos, sensor_dist):
        for x in range(max(0, sensor_pos[0] - sensor_dist), min(sensor_pos[0] + sensor_dist, self.limit)+1):
            if self.dist(sensor_pos, (x, self.y)) <= sensor_dist:
                # self.grid_2[(x, self.y)] = False
                self.set_1.add(x)

    def dist(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def min_max(self, data):
        min_x = data[0][0][0]
        min_y = data[0][1][0]
        max_x = data[0][0][0]
        max_y = data[0][1][0]
        for pair in data:
            for location in pair:
                min_x = min(min_x, location[0])
                min_y = min(min_y, location[1])
                max_x = max(max_x, location[0])
                max_y = max(max_y, location[1])
        return [min_x, max_x, min_y, max_y]

    def add_sensor(self, sensor_location):
        self.grid_2[sensor_location] = 'S'

    def add_beacon(self, beacon_location):
        self.grid_2[beacon_location] = 'B'

    def pos_not_in_row(self):
        count = 0
        for x in range(self.min_x - self.max_dist, self.max_x + self.max_dist):
            if (x, self.y) in self.grid_2:
                if self.grid_2[(x, self.y)] == '#':
                    count += 1
        return count

    def find_point(self):
        for x in range(0, self.limit+1):
            # print((x, self.y))
            if x not in self.set_1:
                return x * 4000000 + self.y
        return False

if __name__ == '__main__':
    with open('input-files/day15.txt') as f:
        data = f.read()

    data = data.replace(',', '').replace(':', '').split('\n')[:-1]
    data = [i.split() for i in data]

    data = [[(int(i[2][2:]), int(i[3][2:])), (int(i[8][2:]), int(i[9][2:]))] for i in data]

    for i in range(4000000):
        print("------------------------------------------------")
        print("------------------------------------------------")
        print("------------------------------------------------")
        print(f"Starting row {i}")
        alpha = grid(data, 4000000, i)
        row_result = alpha.find_point()
        if row_result == False:
            print(f"Row {i} does not have the location required")
        else:
            print(row_result)
            break
    # print(alpha.pos_not_in_row())