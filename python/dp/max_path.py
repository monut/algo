# find the max value travelling from top left cell to the bottom right cell
def max_path(grid):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    # initialize the matrix to 0s
    dp_matrix =  [[0 for _ in range(cols + 1)] for _ in range(rows + 1) ]
    for row in range(rows-1, -1, -1):
        for col in range(cols-1, -1, -1):
            dp_matrix[row][col] =  max(dp_matrix[row+1][col], \
                                       dp_matrix[row][col+1]) \
                                          + grid[row][col]
    print(dp_matrix)
    return dp_matrix[0][0]
 
rows = 4
cols = 5
a = [
    [5, 16, 51, 0],
    [1,84,36,15],
    [65,18, 24, 19],
    [100, 24, 0, 21],
]
print(max_path(a))
