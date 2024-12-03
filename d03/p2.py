#! /usr/bin/python3

import re
INPUTFILE = "use"


with open(INPUTFILE) as fp:
    total = 0
    string = fp.read().replace('\n', '')
    line = ""

    if re.search(r'^(.*?)don\'t\(\)(.*)$', string):
        while m := re.search(r'^(.*?)don\'t\(\)(.*)$', string):
            line += m.group(1)
            string = ""
            maybe = m.group(2)
            if n := re.search(r'^(.*?)do\(\)(.*)$', maybe):
                if re.search(r'^(.*?)don\'t\(\)(.*)$', n.group(2)):
                    string = n.group(2)
                else:
                    line += n.group(2)
    else:
        line = string

    for pairs in [list(map(int, (x.group(1), x.group(2))))
                  for x in re.finditer(r'mul\((\d+),(\d+)\)', line)]:
        total += pairs[0] * pairs[1]
print(total)
