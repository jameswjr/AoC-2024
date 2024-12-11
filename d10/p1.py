#! /usr/bin/python3

from collections import deque

# boilerplate bfs code produced from my personal stash
def bfs(fgrid, start, dest):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set([start])

    while queue:
        (x, y) = queue.popleft()
        if (x, y) == dest:
            return True

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and \
            fgrid[nx][ny] == fgrid[x][y] + 1 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
    return False

grid = []
INPUTFILE = "use"
with open(INPUTFILE) as fp:
    while line := fp.readline().strip():
        nums = []
        for num in line:
            nums.append(int(num))
        grid.append(nums)

print(grid)
trailheads = []
trailfeet = []
for rownum in range(len(grid)):
    for colnum in range(len(grid[0])):
        if grid[rownum][colnum] == 0:
            trailheads.append((rownum, colnum))
        elif grid[rownum][colnum] == 9:
            trailfeet.append((rownum, colnum))

score = 0

for trailhead in trailheads:
    print("Trying trailhead: " + str(trailhead))
    for trailfoot in trailfeet:
        if bfs(grid, trailhead, trailfoot):
            score += 1
    print(score)
