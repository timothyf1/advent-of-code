import re

with open("input/day1.txt") as f:
    raw = f.read()

numsString = {
    "one" : "o1e",
    "two" : "t2o",
    "three" : "th3e",
    "four" : "f4r",
    "five" : "f5e",
    "six" : "s6x",
    "seven" : "s7n",
    "eight" : "e8t",
    "nine" : "n9e"
}

data = []
for line in raw[:-1].split("\n"):
    for string, value in numsString.items():
        line = line.replace(string, value)

    data.append(line)

# print(data)
nums_raw = [re.findall(r'\d', i) for i in data]
# print(nums_raw)
nums = [int(i[0]+i[-1]) for i in nums_raw]
print(nums)
total = sum(nums)

print(total)
