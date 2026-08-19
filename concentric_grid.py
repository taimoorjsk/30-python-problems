# Problem: Concentric Grid
# Create an m x n grid where each cell value represents its layer depth from the
# nearest edge. Center cells have the highest values; edge cells are always 1.

def create_grid(m, n):
    return [[min(r, n - 1 - r, c, m - 1 - c) + 1 for c in range(m)] for r in range(n)]

grid = create_grid(10, 9)

for row in grid:
    print(row)
