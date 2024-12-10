#! /usr/bin/python3

INPUTFILE = "use"
with open(INPUTFILE) as fp:
    nums = []
    calibration = 0

    while line := fp.readline().strip():
        result = int(line.split(':')[0])
        nums = list(map(int, line.split()[1:]))

        count = 0
        while count < 2 ** (len(nums) - 1):
            ops = str(bin(count + 2 ** len(nums)))[3:]
            count += 1
            total = 0
            for i in range(len(nums)):
                if ops[i] == "0":
                    total += nums[i]
                else:
                    total *= nums[i]
            if result == total:
                break

        if total == result:
            print(total, ops, nums)
            calibration += total

print(calibration)
