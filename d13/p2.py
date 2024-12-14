#! /usr/bin/python3

import re
from math import gcd

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

def max_b_solution(my_b, coefficients, goal):
    # prioritize b
    a_c = coefficients[0]
    b_c = coefficients[1]
    interval = a_c / gcd(a_c, b_c)
    found = False
    while not found and interval > 0:
        my_a = (goal - (my_b * b_c)) // a_c
        if my_a * a_c + my_b * b_c == goal:
            found = True
        else:
            my_b -= 1
        interval -= 1
    if not found:
        print ("Could not solve for ", coefficients, goal)
        return False
    return (my_a, my_b)

for machine in machines:
    a_x, a_y = machine[0]
    b_x, b_y = machine[1]
    goal_x, goal_y = machine[2]
    goal_x += 10000000000000
    goal_y += 10000000000000

    max_a = min(goal_x // a_x, goal_y // a_y)
    max_b = min(goal_x // b_x, goal_y // b_y)

    # We have a system of two Diophantine equations, admitting
    # only positive solutions for our unknowns, A and B:
    #
    # 1. a_x * A + b_x * B = goal_x
    # 2. a_y * A + b_y * B = goal_y
    #
    # Each equation, on its own, has a solution iff goal is multiple
    # of the gcd of the given a_*, b_* coefficients (call the gcd "d").
    #
    # Once we know that each has a solution, values of A and B solving
    # both can only be found if there is overlap in the solution sets.
    # If (A, B) is a solution for either equation, it is one of the set
    # of solutions to that equation given by:
    #
    #   A + k * b / d, B - k * a / d
    #
    # Therefore, solutions can be found within min(a/d, b/d) of a
    # starting guess.

    # Are there any solutions for both equations?
    dx = gcd(a_x, b_x)
    dy = gcd(a_y, b_y)

    if goal_x % dx != 0 or goal_y % dy != 0:
        # At least one has no solution
        print("No solution is possible")
        continue

    # Get maximum B value with A, B solving for X and Y, separately:
    A_x, B_x = max_b_solution(max_b, (a_x, b_x), goal_x)
    A_y, B_y = max_b_solution(max_b, (a_y, b_y), goal_y)

    # Check if they overlap by good luck, or seek an integer intersection:
    if B_y == B_x and A_y == A_x:
        # If the points are the same, by construction they yield the largest B:
        cost += 3 * A_x + B_y
        print ("Solved with A, B", A_x, B_y)
        continue

    # A_x * a_x + B_x * b_x = goal_x
    # A_y * a_y + B_y * b_y = goal_y
    #
    # Setting A as the dependent variable in slope-intercept form,
    #  an intersection satisfies the following:
    #
    #   A = B * (-b_x / a_x) + (goal_x / a_x)
    #   A = B * (-b_y / a_y) + (goal_y / a_y)
    #
    # These values of B and A must be the same, so we can subtract:
    #   B * (b_y / a_y - b_x / a_x) + goal_x / a_x - goal_y / a_y = 0
    #
    # Solve for B:
    #   B = (goal_y / a_y - goal_x / a_x) / (b_y / a_y - b_x / a_x)
    #
    # Simplify and cross-multiply, so this ratio should be an int:
    B = (goal_y * a_x - goal_x * a_y) / (b_y * a_x - b_x * a_y)

    # This also should be an int:
    A = (goal_x - B * b_x)/ a_x
    if B == int(B) and B >= 0 and A == int(A) and A >= 0:
        cost += 3 * int(A) + int(B)
        print("Solved (uniquely) with A, B; (machine)", A, B, machine)
        continue
    print("No integer solution found")

print(cost)
