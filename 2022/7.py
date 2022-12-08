with open("input-files/day7.txt") as f:
    data = f.read()

inp = data.split("\n")[:-1]

dir_file_size = {"/r":0}
path = ""

for line in inp:
    parts = line.split()

    # Moving between directorys
    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "/":
                path = "/r"
            elif parts[2] == "..":
                path = path[0:path.rfind("/")]
            else:
                path += f"/{parts[2]}"
                dir_file_size[path] = 0
        continue

    elif parts[0] == "dir":
        continue

    amount = int(parts[0])

    # Adding the size of the file to each parent folder
    dictLoc = path
    for i in range(path.count("/")):
        dir_file_size[dictLoc] += amount
        dictLoc = dictLoc[:dictLoc.rfind("/")]
    
folders_under_100000 = 0
min_deleted = dir_file_size["/r"] - 40000000
possible_folders = []
for directory in dir_file_size:
    if dir_file_size[directory] < 100000:
        folders_under_100000 += dir_file_size[directory]
    if min_deleted <= dir_file_size[directory]:
        possible_folders.append(dir_file_size[directory])

print(folders_under_100000)
print(min(possible_folders))