#! /usr/bin/python3

INPUTFILE = "use"

def blink (stone, memo):
    if stone not in memo:
        count = 5
        stones = [ stone ]
        while count > 0:
            i = 0
            while i < len(stones):
                digits = len(str(stones[i]))
                if digits % 2 == 0:
                    tenexp = 10**(digits/2)
                    stones.insert(i + 1, int(stones[i] % tenexp))
                    stones[i] = int(stones[i] / tenexp)
                    i += 1
                elif stones[i] == 0:
                    stones[i] = 1
                else:
                    stones[i] *= 2024
                i += 1
            count -= 1
        memo[stone] = [len(stones), stones]
    return memo[stone]

def count_stones (stonelist, fmymemo, iters):
    i = 0
    mult = {}
    uselist = stonelist.copy()
    for stone in uselist:
        if stone in mult:
            mult[stone] += 1
        else:
            mult[stone] = 1
    while i < iters:
        bmult = {}
        i += 1
        for stone in mult:
            for bstone in blink(stone, fmymemo)[1]:
                if bstone in bmult:
                    bmult[bstone] += mult[stone]
                else:
                    bmult[bstone] = mult[stone]
        mult = bmult
        uselist = mult.keys()

    total = 0
    for bstone in mult:
        total += mult[bstone]
    return total

with open(INPUTFILE) as fp:
    nums = []

    while line := fp.readline().strip():
        nums = list(map(int, line.split()))

    mymemo = {}
    print("Part 1")
    print(count_stones(nums, mymemo, 5))
    print("Part 2")
    print(count_stones(nums, mymemo, 15))
