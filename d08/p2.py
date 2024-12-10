#! /usr/bin/python3

from math import gcd

INPUTFILE = "use"

with open(INPUTFILE) as fp:
    maxlen = 0
    lines = []
    while line := fp.readline().strip():
        lines.append(line)
        if len(line) > maxlen:
            maxlen = len(line)

antennae = {}

# iterate over lines by index
for linedex in range(len(lines)):
    # iterate over characters by index
    for chardex in range(maxlen):
        char = lines[linedex][chardex]
        if char != ".":
            if char in antennae:
                antennae[char].append((linedex, chardex))
            else:
                antennae[char] = [(linedex, chardex)]

antinodes = set()
for char in antennae:
    for i in range(len(antennae[char]) - 1):
        for j in range(i+1, len(antennae[char])):
            antinodes.add(antennae[char][i])
            dy = antennae[char][j][1] - antennae[char][i][1]
            dx = antennae[char][j][0] - antennae[char][i][0]
            # find all integer points on this line
            # reduce dy/dx
            ldy = dy/gcd(dy, dx)
            ldx = dx/gcd(dy, dx)
            newx, newy = antennae[char][i]
            inbounds = True
            while inbounds:
                newx -= ldx
                newy -= ldy
                if newx > -1 and newx < maxlen and newy > -1 and newy < len(lines):
                    antinodes.add((newx, newy))
                else:
                    inbounds = False
            newx, newy = antennae[char][i]
            inbounds = True
            while inbounds:
                newx += ldx
                newy += ldy
                if newx > -1 and newx < maxlen and newy > -1 and newy < len(lines):
                    antinodes.add((newx, newy))
                else:
                    inbounds = False

print(len(antinodes))
