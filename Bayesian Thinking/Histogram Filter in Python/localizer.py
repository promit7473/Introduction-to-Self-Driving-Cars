import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

#Normalizations
def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    height = len(grid)
    width = len(grid[0])
    total = 0.0
    
    for i in range(height):
        row = []
        for j in range(width):
            hit = (color == grid[i][j])
            row.append(beliefs[i][j] * (hit * p_hit + (1 - hit) * p_miss))
            total += row[j]
        new_beliefs.append(row)
        
    for r in range(height):
        for c in range(width):
            new_beliefs[r][c] = new_beliefs[r][c] / total                       

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
#             pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)