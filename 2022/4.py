with open("input-files/day4.txt") as f:
    data = f.read()

def assigment_set(l1):
    start_end = l1.split("-")
    return set(range(int(start_end[0]), int(start_end[1])+1))

inp = data.split("\n")[:-1]
inp = [i.split(",") for i in inp]
pair_sets = [[assigment_set(i[0]), assigment_set(i[1])] for i in inp]

def subset(sets):
    if sets[0].issubset(sets[1]):
        return True
    if sets[1].issubset(sets[0]):
        return True
    return False

sub_sets_pair = [i for i in pair_sets if subset(i)]
print(len(sub_sets_pair))

def any_common_areas(sets):
    if len(sets[0].intersection(sets[1])) != 0:
        return True
    return False

any_com = [i for i in pair_sets if any_common_areas(i)]

print(len(any_com))
