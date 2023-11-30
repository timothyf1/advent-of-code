

if __name__ == '__main__':
    with open('sample/day16.txt') as f:
        data = f.read()

    data = data.split('\n')[:-1]
    data = [i.split() for i in data]

    data = {i[1]: {'flow_rate':i[4].split('=')[1], 'leads':i[9:]} for i in data}
    print(data)