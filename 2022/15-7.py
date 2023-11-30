class grid():

    def __init__(self, data, limit, y):
        self.grid_2 = {}
        # self.set_1 = set()
        self.set_2 = set(range(limit+1))
        self.min_x, self.max_x, self.min_y, self.max_y = self.min_max(data)
        self.max_dist = 0
        self.y = y
        self.limit = limit
        self.sensor_loc_dist = []
        # print(self.set_2)
        for pair in data:
            # print(f"Starting pair {pair}")
            # self.add_sensor(pair[0])
            # self.add_beacon(pair[1])
            pair_distance = self.dist(pair[0], pair[1])
            self.sensor_loc_dist.append([pair[0], pair_distance])
            y_dist = abs(self.y - pair[0][1])
            max_x_dist = pair_distance - y_dist
            # print(f"Distance is {pair_distance}, y dist {y_dist}, max x dist {max_x_dist}")
            # self.max_dist = max(self.max_dist, pair_distance)
            self.pos_within_range_2(pair[0], max_x_dist, y_dist)
        # print(self.set_2)
        self.smallest_dist = min([i[1] for i in self.sensor_loc_dist])
        # print("Finshed creating set")
        # self.pos_within_range(data[6][0], 9)

    def pos_within_range_2(self, sensor_pos, max_x_dist, y_dist):
        # for x in range(max(0, sensor_pos[0] - max_x_dist), min(sensor_pos[0] + max_x_dist, self.limit)):
            # if self.dist(sensor_pos, (x, self.y)) <= sensor_dist:
                # self.grid_2[(x, self.y)] = False
            # self.set_1.add(x)
        seta = set([i for i in range(sensor_pos[0]-max_x_dist, sensor_pos[0]+max_x_dist+1)])
        # print(seta)
        # self.set_1 = self.set_1.union(seta)
        # print(self.set_2)
        self.set_2 = self.set_2.difference(seta)
        # print(self.set_2)
        # print([i for i in range(sensor_pos[0]-max_x_dist, sensor_pos[0]+max_x_dist+1)])

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
        # for x in range(0, self.limit+1):
        #     # print((x, self.y))
        #     if x in self.set_2:
        #         print((x, self.y))
        #         return x * 4000000 + self.y
        # return False
        if len(self.set_2) == 0:
            return False
        return list(self.set_2)[0] * 4000000 + self.y

    def min_y_diff(self):
        def sensor_range(sensor):
            dist_i = []
            for i in [0, self.limit]:
                dist = self.dist(sensor[0], (i, self.y))
                if dist < sensor[1]:
                    dist_i.append(sensor[1] - dist)
                else:
                    print(f"returning with sensor {sensor} at point {i, self.y}, dist {dist}")
                    return 0
            print("test")
            return min(dist_i) if len(dist_i) > 0 else 0

        sensors_min_y = []
        for sensor in self.sensor_loc_dist:
            sensors_min_y.append(sensor_range(sensor))
        if len(sensors_min_y) == 0:
            return 0
        return max(sensors_min_y)

if __name__ == '__main__':
    with open('input-files/day15.txt') as f:
        data = f.read()

    data = data.replace(',', '').replace(':', '').split('\n')[:-1]
    data = [i.split() for i in data]

    data = [[(int(i[2][2:]), int(i[3][2:])), (int(i[8][2:]), int(i[9][2:]))] for i in data]
    skip = set()
    for i in range(4000000):
        if i in skip:
            continue
        # print("------------------------------------------------")
        # print("------------------------------------------------")
        print("------------------------------------------------")
        print(f"Starting row {i}")
        alpha = grid(data, 4000000, i)
        row_result = alpha.find_point()
        if row_result == False:
            print(f"Row {i} does not have the location required")
            num_to_skip = alpha.min_y_diff()
            print(f"Rows to skipt {num_to_skip}")
            skip = skip.union(set(range(i, i + num_to_skip + 1)))
            # print(skip)
        else:
            print(row_result)
            break
    # print(alpha.pos_not_in_row())