#! /usr/bin/python3

INPUTFILE = "use"

def check_order(fpages):
    for page in fpages:
        pagedict[page] = 1

    for pagedex in range(len(fpages)):
        hasreq = True
        if fpages[pagedex] in rules:
            prereqs = []
            for req in (rules[fpages[pagedex]]):
                if req in pagedict:
                    prereqs.append(req)

            for req in prereqs:
                hasreq = False
                for checkdex in range(pagedex):
                    if fpages[checkdex] == req:
                        hasreq = True
                        break
                if not hasreq:
                    break
        if not hasreq:
            break

    if not hasreq:
        fnewpages = fpages.copy()
        fnewpages.remove(req)
        fnewpages.insert(pagedex, req)
        return fnewpages
    return True

with open(INPUTFILE) as fp:
    rules = {}
    midsum = 0

    while line := fp.readline().strip():
        (first, second) = list(map(int, line.split("|")))
        if second in rules:
            rules[second].append(first)
        else:
            rules[second] = [first]

    while line := fp.readline().strip():
        pages = []
        pagedict = {}
        pages = list(map(int, line.split(",")))

        newpages = check_order(pages)
        if newpages is True:
            print("Correctly ordered update: "  + str(pages))
        else:
            print("Incorrect")
            while newpages is not True:
                pages = newpages
                newpages = check_order(newpages)
            print("Fixed order pages: " + str(pages))
            midsum += pages[int(len(pages)/2)]

print(midsum)
