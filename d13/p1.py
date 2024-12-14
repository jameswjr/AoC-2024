#! /usr/bin/python3

import re

INPUTFILE = "use"

with open(INPUTFILE) as fp:
    machines = []

    machine = []
    while line := fp.readline():
        if matches := re.search(r'X.(\d+), Y.(\d+)', line):
            machine.append((int(matches.group(1)), int(matches.group(2))))
        else:
            machines.append(machine)
            machine = []
            continue
if len(machine) > 0:
    machines.append(machine)

cost = 0

for machine in machines:
    a_x, a_y = machine[0]
    b_x, b_y = machine[1]
    goal_x, goal_y = machine[2]

    max_a = min(goal_x // a_x, goal_y // a_y)
    max_b = min(goal_x // b_x, goal_y // b_y)

    temp_b = max_b
    temp_a = 0
    optimum = False
    gap_x = 0
    gap_y = 0
    steps = 0
    while not optimum and temp_b >= 0 and temp_a <= max_a:
        gap_x = goal_x - temp_a * a_x - temp_b * b_x
        gap_y = goal_y - temp_a * a_y - temp_b * b_y
        while gap_x >= a_x and gap_y >= a_y:
            temp_a += 1
            gap_x = goal_x - temp_a * a_x - temp_b * b_x
            gap_y = goal_y - temp_a * a_y - temp_b * b_y
        if gap_x == 0 and gap_y == 0:
            print("A solution found: ", temp_a, " ", temp_b, " ", machine)
            optimum = True
            cost += 3 * temp_a + temp_b
        else:
            temp_b -= 1
            gap_x = goal_x - temp_a * a_x - temp_b * b_x
            gap_y = goal_y - temp_a * a_y - temp_b * b_y

    if not optimum:
        print("No solution found: ", machine, temp_a, temp_b)

print(cost)
