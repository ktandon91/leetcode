from graph import graph_bfs

g = graph_bfs() # 5 nodes

def solve(s):
    q = []
    q.append(s)
    
    visited = [False for _ in range(g.vertices)]
    prev = [None for _ in range(g.vertices)]
    
    visited[s] = True
    while q:
        node = q.pop(0)
        print(f'Visiting {node}')
        neighbours = g.adjacency_list[node]
        for neighbour in neighbours:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)
                prev[neighbour]=node
    return prev

def reconstruct_path(s, e, prev):
    path = []
    while e != None:
        path.append(e)
        e = prev[e]
    path = list(reversed(path))
    
    # check if start is connected to
    if path[0] == s:
        return path
    return []

    

# bfs from start node to end node
def bfs(s, e):
    # do a bfs on starting node
    prev = solve(s)
    #reconstruct path from s->e
    return reconstruct_path(s, e, prev)

print(bfs(3,5))
