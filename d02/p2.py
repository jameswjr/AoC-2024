#! /usr/bin/python3

def check_safe(levels):
    sign = 0
    prev = None
    good = True
    col = -1
    for num in levels:
        col += 1
        if prev is None:
            prev = num
            continue

        delta = prev - num
        prev = num
        if delta == 0:
            good = False
            break
        if sign == 0:
            sign = delta / abs(delta)
        if delta / sign < 1 or delta / sign > 3:
            good = False
            break

    if good:
        return good
    return col

INPUTFILE = "use"
with open(INPUTFILE) as fp:
    nums = []
    safes = 0

    while line := fp.readline().strip():
        nums = list(map(int, line.split()))
        safe = check_safe(nums)
        print(nums, safe)
        if safe is True:
            safes += 1
        elif safe == len(nums) - 1:
            # if the last element is unsafe, it can be removed
            safes += 1
            print("But safe!")
        else:
            for offset in (-2, -1, 0):
                # Case analysis of how a single removal can mend a level:
                # try removing element two back to address a special case of
                #   changing direction (sign) after the first two elements
                # all others can be mended only by removing either the prior
                # element, or the flagged element itself
                if offset == -2 and safe != 2:
                    # skip offset -2 if not in column 3 (index 2)
                    continue
                removal = safe + offset
                smaller = nums[:removal].copy()
                smaller.extend(nums[removal + 1:])
                if check_safe(smaller) is True:
                    safes += 1
                    print("Reduced list from unsafe to safe: ", nums, smaller,
                           offset)
                    break

print(safes)
