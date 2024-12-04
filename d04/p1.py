#! /usr/bin/python3

INPUTFILE = "use"

with open(INPUTFILE) as fp:
    xmas = 0
    maxlen = 0
    lines = []
    while line := fp.readline().strip():
        lines.append(line)
        if len(line) > maxlen:
            maxlen = len(line)

# iterate over lines by index
for linedex in range(len(lines)):
    # iterate over characters by index
    for chardex in range(maxlen):
        # try all directions r, dr, d, dl, l, ul, u, ur
        for direction in (0,1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1):
            curline = linedex
            curchar = chardex
            # assemble the string in all directions -- skip if impossible
            xmas += 1
            for char in "XMAS":
                if lines[curline][curchar] != char:
                    xmas -= 1
                    break
                if char == "S":
                    break
                curline += direction[0]
                curchar += direction[1]
                if curline < 0 or curline > (len(lines) - 1):
                    xmas -= 1
                    break
                if curchar < 0 or curchar > (len(lines[curline]) - 1):
                    xmas -= 1
                    break

print(xmas)
