#! /usr/bin/python3

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
            dx = antennae[char][j][0] - antennae[char][i][0]
            dy = antennae[char][j][1] - antennae[char][i][1]
            for antinode in [(antennae[char][i][0] - dx, antennae[char][i][1] - dy),
                             (antennae[char][j][0] + dx, antennae[char][j][1] + dy)]:
                if antinode[0] > -1 and antinode[0] < maxlen and \
                   antinode[1] > -1 and antinode[1] < len(lines):
                    antinodes.add(antinode)

print(len(antinodes))
print(antinodes)
