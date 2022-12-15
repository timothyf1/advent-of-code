class grid():

    def __init__(self, data, limit):
        self.grid_2 = {}
        self.min_x, self.max_x, self.min_y, self.max_y = self.min_max(data)
        self.max_dist = 0
        self.limit = limit

        for pair in data:
            print(f"Starting pair {pair}")
            self.add_sensor(pair[0])
            self.add_beacon(pair[1])
            pair_distance = self.dist(pair[0], pair[1])
            self.max_dist = max(self.max_dist, pair_distance)
            self.pos_within_range_2(pair[0], pair_distance)
            
        print("Finished adding to dict")
        # self.pos_within_range(data[6][0], 9)

    def pos_within_range_2(self, sensor_pos, sensor_dist):
        for x in range(max(0, sensor_pos[0] - sensor_dist -1), min(sensor_pos[0] + sensor_dist, self.limit+1)):
            for y in range(max(0, sensor_pos[1] - sensor_dist -1), min(sensor_pos[1] + sensor_dist, self.limit+1)):
                if (x, y) not in self.grid_2:
                    if self.dist(sensor_pos, (x, y)) <= sensor_dist:
                        self.grid_2[(x, y)] = '#'

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
            for y in range(0, self.limit+1):
                print((x, y))
                if (x, y) not in self.grid_2:
                    return x * 4000000 + y

if __name__ == '__main__':
    with open('input-files/day15.txt') as f:
        data = f.read()

    data = data.replace(',', '').replace(':', '').split('\n')[:-1]
    data = [i.split() for i in data]
    data = [[(int(i[2][2:]), int(i[3][2:])), (int(i[8][2:]), int(i[9][2:]))] for i in data]

    alpha = grid(data, 4000000)
    # print(alpha.pos_not_in_row())
    print(alpha.find_point())