#! /usr/bin/python3

import re

INPUTFILE = "use"
total = 0
llist = []
rdict = {}
with open(INPUTFILE) as fp:
    while line := fp.readline().strip():
        matches = re.search(r'(\d+).*?(\d+)', line)
        llist.append(int(matches.group(1)))
        if int(matches.group(2)) in rdict:
            rdict[int(matches.group(2))] += 1
        else:
            rdict[int(matches.group(2))] = 1

for num in llist:
    if num in rdict:
        total += num * rdict[num]

print(total)
