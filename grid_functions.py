def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width
        grid += [row]

    return grid


def copy(grid):
    """ copies the entirety of a grid into a secondary grid avoiding copying the reference """
    c_grid = create_grid(len(grid),len(grid[0]))
    
    for c in range(len(grid[0])):
        for r in range(len(grid)):
            c_grid[r][c] = grid[r][c]
            
    return c_grid

def alive_neighbors(posnr, posnc, grid):
    """ counts the number of cells that are 1 surrouding position (posnr,posnc) """
    alive_count = 0
    l = range(-1,2)
    
    for c in l:
        for r in l:
            if grid[(posnr + r) % len(grid)][(posnc + c) % len(grid[0])] == 1:
                if r != 0 or c != 0:
                    alive_count += 1
    
    return alive_count


def next_gen(grid):
    """ creates the next generation according to the game rules """
    new_grid = copy(grid)
    
    h_border = len(grid) - 1
    w_border = len(grid[0]) - 1
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if alive_neighbors(r,c,grid) == 3:
                new_grid[r][c] = 1
            elif alive_neighbors(r,c,grid) > 3 or alive_neighbors(r,c,grid) < 2:
                new_grid[r][c] = 0
                    
    return new_grid