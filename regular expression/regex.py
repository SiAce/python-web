import re

with open("README.md") as test:
    for line in test:
        line = line.rstrip()
        if re.search("python", line):
            print(re.findall("python", line))
