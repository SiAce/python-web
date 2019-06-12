import re

sum = 0

with open("regex_sum_247998.txt") as text:
    for line in text:
        line = line.rstrip()
        num_array = re.findall("[0-9]+", line)
        for num in num_array:
            sum += int(num)

print(sum)
