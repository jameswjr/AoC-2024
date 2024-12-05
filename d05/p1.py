#! /usr/bin/python3

INPUTFILE = "use"

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
        for page in pages:
            pagedict[page] = 1

        for pagedex in range(len(pages)):
            hasreq = True
            if pages[pagedex] in rules:
                prereqs = []
                for req in (rules[pages[pagedex]]):
                    if req in pagedict:
                        prereqs.append(req)

                for req in prereqs:
                    hasreq = False
                    for checkdex in range(pagedex):
                        if pages[checkdex] == req:
                            hasreq = True
                            break
                    if not hasreq:
                        print("Pages fails missing prereq for " + str(pages[pagedex]))
                        break
            if not hasreq:
                break
        if hasreq:
            print("Correctly ordered update: "  + str(pages))
            midsum += pages[int(len(pages)/2)]

print(midsum)
