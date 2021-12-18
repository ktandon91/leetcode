grid = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'E', '.', '#', '.']
]

#Global Variables
# Rows and columns in a Grid
R = len(grid)
C = len(grid[0])
sr , sc = 0, 0 # Start Row and Start column
rq, cq = [], [] # row and column queues for tracing the neighbours

#Variables used to track number of steps taken
move_count = 0 # move_counter to track moves
nodes_left_in_layer = 1 # intializing it to one since start will be the only node in the beiginning
nodes_in_next_layer = 0

# Variable to track end of the matrix
reached = False

# Variable to track status of a node, if already visited or not
visited = [[False for col in range(C)] for row in range(R)]

# Direction vectors
dr = [-1, +1, 0, 0] # North South East West
dc = [0, 0, +1, -1]

def explore_neighbours(r,c):
    global nodes_in_next_layer

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        # Check if matrix is out of bound
        if rr < 0 or cc < 0: continue
        if rr >= R or cc >= C: continue

        # Check if cell is already visited
        if visited[rr][cc]: continue
        # Check if cell is a bloacked path
        if grid[rr][cc] == '#': continue 

        # Add neighbour to the queue
        rq.append(rr)
        cq.append(cc)
        visited[rr][cc] = True
        nodes_in_next_layer += 1

def solve():
    global nodes_left_in_layer, nodes_in_next_layer, move_count
    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True
    while rq:
        r = rq.pop(0)
        c = cq.pop(0)
        if grid[r][c] == 'E':
            reached = True
            break
        explore_neighbours(r,c)
        nodes_left_in_layer-=1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count+=1
    if reached:
        return move_count
    return -1

print(solve())
