#! /usr/bin/python3

INPUTFILE = "use"

with open(INPUTFILE) as fp:
    total = 0
    string = fp.read()

    if len(string) % 2 == 0:
        string = string[:-1] # take off any trailing free space

    target = 1
    move = len(string) - 1
    checksum = 0
    position = int(string[0])

    used = 0

    compacted = False

    while not compacted:
        tomove = int(string[move])
        block = move / 2
        blockmoved = 0

        while tomove > 0 and not compacted:
            skipped = 0
            moved = 0
            if tomove <= int(string[target]) - used:
                used += tomove
                if used == int(string[target]):
                    used = 0
                    target += 2
                    skipped = int(string[target - 1])
                moved = tomove
                blockmoved += moved
                tomove = 0
            else:
                moved = int(string[target]) - used
                blockmoved += moved
                tomove -= moved
                used = 0
                target += 2
                skipped = int(string[target - 1])
            if skipped > 0:
                skipblock = target / 2 - 0.5
                skippos = position + moved
                if skipblock >= block:
                    skipped -=  blockmoved
                    compacted = True

                checksum += skipblock * (skippos * skipped + ((skipped-1)**2 \
                                                              + skipped - 1)/2)

            checksum += block * (position * moved  + ((moved - 1)**2 + \
                                                      moved - 1)/2)
            position += moved + skipped
            print("Checksum: " + str(checksum))

        move -= 2

    print(checksum)
