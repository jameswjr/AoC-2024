#! /usr/bin/python3

grid = []
INPUTFILE = "use"
with open(INPUTFILE) as fp:
    while line := fp.readline().strip():
        chars = []
        for char in line:
            chars.append(char)
        grid.append(chars)

rmap = {}
regions = {}
region_id = 0

def create_region(frmap, fregion_id, crop, fperimeter, cell):
    # region id, crop, perimeter count, array of cells
    frmap[(cell[0], cell[1])] = fregion_id
    regions[fregion_id] = [crop, fperimeter, [cell]]
    return fregion_id

def merge_region(old, new, frmap):
    if old == new:
        return old
    # merge region adds two regions of same plant that touch
    regions[old][1] += regions[new][1]

    regions[old][2].extend(regions[new][2])
    for cell in regions[new][2]:
        frmap[cell] = old
    del regions[new]
    return old

# iterate over cells
for row in range(len(grid)):
    for col in range(len(grid[0])):
        connect_left = False
        connect_up = False
        perimeter = 4
        plant = grid[row][col]
        # look left, up for perimeter and a region to connect to;
        # if none, start a new region.
        if col != 0:
            if grid[row][col - 1] == plant:
                perimeter -= 1
                connect_left = True
        if col != len(grid[0]) - 1:
            if grid[row][col + 1] == plant:
                perimeter -= 1
        if row != 0:
            if grid[row - 1][col] == plant:
                perimeter -= 1
                connect_up = True
        if row != len(grid) - 1:
            if grid[row + 1][col] == plant:
                perimeter -= 1
        new_id = create_region(rmap, region_id, plant, perimeter, (row, col))
        region_id += 1
        if connect_up:
            new_id = merge_region(rmap[(row - 1,col)], new_id, rmap)
        if connect_left:
            new_id = merge_region(rmap[(row,col - 1)], new_id, rmap)

# Find all edges:
boundaries = {}

for horizontal in range(len(grid) + 1):
    # go across each row.
    above_region = -1
    this_region = -1
    old_above = -1
    old_this = -1
    for col in range(len(grid[0])):
        # Any region above different from region below
        # is part of a unique boundary for that region
        if horizontal == 0:
            if rmap[(horizontal, col)] == this_region:
                continue
            this_region = rmap[(horizontal, col)]
            if this_region in boundaries:
                boundaries[this_region] += 1
            else:
                boundaries[this_region] = 1
        elif horizontal != len(grid):
            # check above
            old_above = above_region
            above_region = rmap[(horizontal - 1, col)]
            old_this = this_region
            this_region = rmap[(horizontal, col)]
            if this_region != above_region:
                # if either this region is new or it differed before
                if this_region != old_this or old_above == this_region:
                    if this_region in boundaries:
                        boundaries[this_region] += 1
                    else:
                        boundaries[this_region] = 1
                if above_region != old_above or old_this == above_region:
                    if above_region in boundaries:
                        boundaries[above_region] += 1
                    else:
                        boundaries[above_region] = 1
        else:
            if rmap[(horizontal - 1, col)] == above_region:
                continue
            above_region = rmap[(horizontal - 1, col)]
            if above_region in boundaries:
                boundaries[above_region] += 1
            else:
                boundaries[above_region] = 1

for vertical in range(len(grid[0]) + 1):
    # now descend each col. Any region to the right different
    # from that to the left is a boundary for those regions.
    left_region = -1
    this_region = -1
    for row in range(len(grid)):
        # Any region above different from region below
        # is part of a unique boundary for that region
        if vertical == 0:
            if rmap[(row, vertical)] == this_region:
                continue
            this_region = rmap[(row, vertical)]
            if this_region in boundaries:
                boundaries[this_region] += 1
            else:
                boundaries[this_region] = 1

        elif vertical != len(grid[0]):
            # check left
            old_left = left_region
            left_region = rmap[(row, vertical - 1)]
            old_this = this_region
            this_region = rmap[(row, vertical)]
            if this_region != left_region:
                # if either this region is new or it differed before
                if this_region != old_this or old_left == this_region:
                    if this_region in boundaries:
                        boundaries[this_region] += 1
                    else:
                        boundaries[this_region] = 1
                if left_region != old_left or old_this == left_region:
                    if left_region in boundaries:
                        boundaries[left_region] += 1
                    else:
                        boundaries[left_region] = 1
        else:
            if rmap[(row, vertical - 1)] == left_region:
                continue
            left_region = rmap[(row, vertical - 1)]
            if left_region in boundaries:
                boundaries[left_region] += 1
            else:
                boundaries[left_region] = 1

price = 0
for region in regions:
    price += boundaries[region] * len(regions[region][2])

print(price)
