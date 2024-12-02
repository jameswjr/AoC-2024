#! /usr/bin/python3

import re

INPUTFILE = "use"
total = 0
llist = []
rlist = []
with open(INPUTFILE) as fp:
    while line := fp.readline().strip():
        matches = re.search(r'(\d+).*?(\d+)', line)
        llist.append(int(matches.group(1)))
        rlist.append(int(matches.group(2)))

sllist = sorted(llist)
srlist = sorted(rlist)

for index in range(0, len(sllist)):
    lnum = sllist[index]
    rnum = srlist[index]
    if lnum < rnum:
        total += (rnum - lnum)
    else:
        total += (lnum - rnum)

print(total)
