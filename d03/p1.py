#! /usr/bin/python3

import re
INPUTFILE = "use"

with open(INPUTFILE) as fp:
    total = 0
    while line := fp.readline().strip():
        for pairs in [list(map(int, (x.group(1), x.group(2))))
                      for x in re.finditer(r'mul\((\d+),(\d+)\)', line)]:
            total += pairs[0] * pairs[1]
print(total)
