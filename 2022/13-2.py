from functools import cmp_to_key

with open('input-files/day13.txt') as f:
    data = f.read()

data = data[:-1].replace('\n\n', '\n')

data = [eval(i) for i in data.split('\n')]

data.append([[2]])
data.append([[6]])

def compare(a, b):
    for l, r in zip(a, b):
        if not isinstance(l, list) and isinstance(r, list):
            l = list([l])

        if isinstance(l, list) and not isinstance(r, list):
            r = list([r])

        if isinstance(l, list) and isinstance(r, list):
            res = compare(l, r)
            if res == 0:
                pass
            elif res < 0:
                return -1
            else:
                return 1
        else:
            if l < r:
                return -1
            elif l > r:
                return 1

    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    return 0

order = sorted(data, key=cmp_to_key(compare))

print((order.index([[2]])+1) * (order.index([[6]])+1))