#! /usr/bin/python3

INPUTFILE = "use"

with open(INPUTFILE) as fp:
    nums = []
    safes = 0
    while line := fp.readline().strip():
        sign = 0
        prev = None
        safe = True
        nums = list(map(int, line.split()))
        for num in nums:
            if prev is None:
                prev = num
                continue

            delta = prev - num
            prev = num
            if delta == 0:
                safe = False
                break
            if sign == 0:
                sign = delta / abs(delta)
            if delta / sign < 1 or delta / sign > 3:
                safe = False
                break
        print(nums, safe)
        if safe is True:
            safes += 1

print(safes)
