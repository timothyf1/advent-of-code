from copy import copy
from math import lcm

def round():
    for i in monkey_dict.keys():
        round_start_items = copy(monkey_dict[i]["items"])
        monkey_dict[i]['inspected'] += len(round_start_items) 
        for item in round_start_items:
            old = item % div_lcm 
            new = eval(monkey_dict[i]["operation"])
            # Add following line for part 1
            # new = new // 3  
            if new % monkey_dict[i]['test'] == 0:
                monkey_dict[i]['items'].remove(item)
                monkey_dict[monkey_dict[i]['monkey_true']]['items'].append(new)
            else:
                monkey_dict[i]['items'].remove(item)
                monkey_dict[monkey_dict[i]['monkey_false']]['items'].append(new)

if __name__ == '__main__':
    with open('input-files/day11.txt') as f:
        data = f.read()

    inp = data.split('\n\n')
    inp = [i.split('\n') for i in inp]

    # Creating monkey dictionary
    monkey_dict = {
                    int(monkey[0].split()[1].split(":")[0]) : 
                        {
                            "items" : [int(i) for i in monkey[1].split(":")[1].split(",")],
                            "operation" : monkey[2].split("=")[1],
                            "test" : int(monkey[3].split()[3]),
                            "monkey_true" : int(monkey[4].split()[5]),
                            "monkey_false" : int(monkey[5].split()[5]),
                            "inspected" : int(0),
                        }
                    for monkey in inp
                }

    # Find LCM for each test divisor
    div = [monkey_dict[monkey]['test'] for monkey in monkey_dict.keys()]
    div_lcm = lcm(*div)

    # 20 rounds for part 1
    # 10000 rounds for part 2
    for i in range(10000):
        round()

    # Finding how many times each monkey inspected an item
    inpected = [monkey_dict[monkey]['inspected'] for monkey in monkey_dict.keys()]
    inpected.sort()
    print(inpected[-1] * inpected[-2])