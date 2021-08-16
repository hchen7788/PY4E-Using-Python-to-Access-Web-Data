import re

file = open("regex_sum_1337535.txt", 'r')

nums = []
for line in file:
    temp = re.findall('[0-9]+', line)
    nums += temp

sum = 0
for i in nums:
  sum += int(i)

print(sum)
