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

            if total != result:
                # Here try to build the new concatenated nums array
                count = 0

                solved = False
                while count < 2 ** (len(nums) - 1) and not solved:
                    ops = str(bin(count + 2 ** len(nums)))[3:]
                    count += 1

                    newcount = 0
                    while newcount < 2 ** (len(nums) - 1):
                        newops = str(bin(newcount + 2 ** len(nums)))[3:]
                        newcount += 1
                        newtotal = 0
                        for i in range(len(nums)):
                            if newops[i] == "0":
                                if ops[i] == "0":
                                    newtotal += nums[i]
                                else:
                                    newtotal *= nums[i]
                            else:
                                newtotal *= 10**(len(str(nums[i])))
                                newtotal += nums[i]

                        if result == newtotal:
                            total = newtotal
                            solved = True
                            break
            if result == total:
                print(result, nums)
                calibration += total
                break

print(calibration)
