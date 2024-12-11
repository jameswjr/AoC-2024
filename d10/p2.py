#! /usr/bin/python3

from collections import deque

# boilerplate bfs code produced from my personal stash
def bfs(fgrid, start, dest):
    rows, cols = len(fgrid), len(fgrid[0])
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

# ditto with dfs code I kept handy for just such a time
def dfs(fgrid, start, end, path, visited):
    x, y = start
    rows, cols = len(fgrid), len(fgrid[0])
    found = 0

    if not (0 <= x < rows and 0 <= y < cols and \
            (len(path) == 1 or fgrid[x][y] - fgrid[path[-2][0]][path[-2][1]] == 1)) or \
            (x, y) in visited:
        return 0
    if (x, y) == end:
        return 1

    visited.add((x, y))
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
        found += dfs(fgrid, (x + dx, y + dy), end, path + [(x + dx, y + dy)], visited)

    visited.remove((x, y))  # Backtrack
    return found

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

rating = 0

for trailhead in trailheads:
    print("Trying trailhead: " + str(trailhead))
    for trailfoot in trailfeet:
        print("Trying trailfoot: " + str(trailfoot))
        rating += dfs(grid, trailhead, trailfoot, [trailhead], set())
        print("Rating so far: " + str(rating))
    print(rating)
