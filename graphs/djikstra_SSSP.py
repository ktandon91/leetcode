# Dijikstra algo is used for single source shortest path
# Used for graphs with non negative nodes

from graph import single_source_shortest_path
from heapq import heappush, heappop

g = single_source_shortest_path()


def dijikstra(g, N, start):
    """
        g: graph
        N: number of nodes
        s: starting node  
    """
    visited = [False for _ in range(N)]
    dis = [float('inf') for _ in range(N)]
    prev = [None for _ in range(N)] # for tracking path
    dis[start] = 0
    q = [] # priority queue will hold tuple of (distance, index)
    heappush(q, (0, start))
    
    while q:
        min_val, idx = heappop(q)
        visited[idx] = True
        if dis[idx] < min_val: # Optimization if min val is greate than dis[idx]
            continue           # then a shortest path is already present
        for edge in g.adjacency_list[idx]:
            if not visited[edge.to]:
                new_dist = dis[idx] + edge.weight
                if new_dist < dis[edge.to]:
                    prev[edge.to] = idx
                    dis[edge.to] = new_dist
                    heappush(q, (new_dist, edge.to))
    return prev,dis

def find_shortest_path(prev, dis, e):
    path = []
    if dis[e] == float('inf'):
        return path
    
    while e is not None:
        path.append(e)
        e = prev[e]
    path.reverse()
    return path

def main():
    N = g.vertices
    prev, dis = dijikstra(g, N, 0)
    print(f"path = {prev}")
    print(f"distance from start node = {dis}")
    path = find_shortest_path(prev, dis, 4)
    print(f"shorted path to 4 -> {path}")
main()

