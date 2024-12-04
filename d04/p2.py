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
for linedex in range(1,len(lines)-1):
    # iterate over characters by index
    for chardex in range(1,maxlen-1):
        # this time, assemble an "X"
        if lines[linedex][chardex] == "A":
            xmas += 1
            for offset in (-1, 1):
                others = {}
                others[lines[linedex+offset][chardex-1]] = 1
                others[lines[linedex-offset][chardex+1]] = 1
                if not ("M" in others and "S" in others):
                    xmas -= 1
                    break

print(xmas)
