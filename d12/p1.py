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
    print()
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
        # my_region = create_region(rmap, plant, 4, ([row, col]))
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


price = 0
for region in regions:
    price += regions[region][1] * len(regions[region][2])
    print(price)
