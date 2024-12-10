#! /usr/bin/python3

INPUTFILE = "use"

guards = {"^": (-1, 0, 0), ">": (0, 1, 1), "v": (1, 0, 2), "<": (0, -1, 3)}
posnum = {0: "^", 1: ">", 2: "v", 3: "<"}

with open(INPUTFILE) as fp:
    maxlen = 0
    lines = []
    while line := fp.readline().strip():
        lines.append(line)
        if len(line) > maxlen:
            maxlen = len(line)

found = False
# iterate over lines by index
for linedex in range(len(lines)):
    # iterate over characters by index
    for chardex in range(maxlen):
        if lines[linedex][chardex] in guards:
            found = True
            break
    if found:
        break

steps = 0

linedel, chardel, pos = guards[lines[linedex][chardex]]
visited = set()

while linedex > -1 and chardex > -1 and linedex < len(lines) and chardex < maxlen:
    visited.add((linedex, chardex))
    nline = linedex + linedel
    nchar = chardex + chardel
    if nline == -1 or nchar == -1 or nline == len(lines) or nchar == maxlen:
        steps += 1
    elif lines[nline][nchar] == "#":
        pos = (pos + 1) % 4
        linedel, chardel, pos = guards[posnum[pos]]
        nline = linedex + linedel
        nchar = chardex + chardex
        continue
    else:
        steps += 1

    print("Step to: " + " ".join((str(nline), str(nchar))))
    linedex = nline
    chardex = nchar

print(steps)        
print(len(visited))        
        
        
