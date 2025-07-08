# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
# Empty positions are marked ..
# Walls are marked W.
# Start and exit positions are empty in all test cases.

# example
# maze = "\n".join([
#         "......",
#         "......",
#         "......",
#         ".....W",
#         
#     ])
#     test.assert_equals(path_finder(maze), False, repr(maze))

def path_finder(maze):
    mazeGrid = maze.split('\n')
    m,n = len(mazeGrid), len(mazeGrid[0])
    stack = [(0,0)]
    seen = set()

    while stack:
        x,y = stack.pop()

        if x == m - 1 and y == n - 1:
            return True
    
        if x >= 0 and x < m and y >= 0 and y < n and (x,y) not in seen and mazeGrid[x][y] == '.':
            seen.add((x,y))
            stack.append((x+1,y))
            stack.append((x-1,y))
            stack.append((x,y+1))
            stack.append((x,y-1))

    return False

maze = "\n".join([
        ".W.",
        ".W.",
        "..."
    ])

print(path_finder(maze))