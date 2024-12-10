#! /usr/bin/python3

INPUTFILE = "use"

with open(INPUTFILE) as fp:
    string = fp.read()
    block = 0
    high = block
    checksum = 0

    # new approach:
    # enumerate (starting / remaining) size of all empty spots,
    #  and their start positions
    # also enumerate all the full blocks and their starting positions
    # calculate checksum on each after they have all moved

    empties = []
    blocks = []
    nextpos = 0
    while block < len(string):
        blocks.append([block//2, int(string[block]), nextpos])
        nextpos += int(string[block])
        block += 1
        high = (block - 1) // 2
        if block < len(string):
            empties.append(['empty', int(string[block]), nextpos])
            nextpos += int(string[block])
            block += 1

    while high > 0:
        for empty in empties:
            if empty[1] >= blocks[high][1] and empty[2] < blocks[high][2]:
                blocks[high][2] = empty[2]
                empty[2] += blocks[high][1]
                empty[1] -= blocks[high][1]
                break
        high -= 1

    for block in blocks:
        num = block[0]
        size = block[1]
        pos = block[2]
        checksum += num * (pos * size + ((size - 1)**2 + size - 1)//2)

    print("Checksum: " + str(checksum))
