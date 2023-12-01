import re

with open("input/day1.txt") as f:
    data = f.read()

data = data[:-1].split("\n")

nums_raw = [re.findall(r'\d', i) for i in data]
print(nums_raw)
nums = [int(i[0]+i[-1]) for i in nums_raw]
print(nums)
total = sum(nums)

print(total)
