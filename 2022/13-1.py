with open('input-files/day13.txt') as f:
    data = f.read()

# print([pair.split('\n') for pair in data[:-1].split('\n\n')])

data = [[eval(j) for j in i.split('\n')] for i in data[:-1].split('\n\n')]

def compare(pair):
    for l, r in zip(pair[0], pair[1]):
        if not isinstance(l, list) and isinstance(r, list):
            l = list([l])

        if isinstance(l, list) and not isinstance(r, list):
            r = list([r])

        if isinstance(l, list) and isinstance(r, list):
            res = compare([l, r])
            if res == None:
                pass
            elif res:
                return True
            else:
                return False
        else:
            if l < r:
                return True
            elif l > r:
                return False

    if len(pair[0]) < len(pair[1]):
        return True
    elif len(pair[0]) > len(pair[1]):
        return False
    return None

sum_1 = 0
for pair, index in zip(data, range(len(data))):
    if compare(pair):
        sum_1 += index+1

print(sum_1)