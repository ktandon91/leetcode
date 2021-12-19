from graph import single_source_shortest_path

g = single_source_shortest_path()

def dfs(at, visited, visited_nodes, graph):
    visited[at] = True
    edges = graph.adjacency_list[at]

    for edge in edges:
        if not visited[edge.to]:
            dfs(edge.to, visited, visited_nodes, graph)
    # post_order.append(at)
    visited_nodes.append(at)

def topsort(g):
    N = g.vertices
    top_ordering = [0 for _ in range(N)] 
    visited = [False for _ in range(N)]
    i = N-1 # Index for maintaining topological ordering
    for at in range(g.vertices):
        if not visited[at]:
            visited_nodes = []
            dfs(at, visited, visited_nodes, g)
            for node in visited_nodes:
                top_ordering[i] = node
                i-=1
    return top_ordering 

def dag_shortest_path(g, start, N):
    # Get shortest path
    top_ordering = topsort(g) #[6, 0, 5, 1, 2, 3, 4]
    # Initialize distance list None indicates no direct 
    # path between start and the particular node
    dist = [None for _ in range(N)]
    dist[start] = 0

    for i in range(N):
        node_idx = top_ordering[i]
        if dist[node_idx] is not None:
            edges = g.adjacency_list[node_idx]
            if edges:
                for edge in edges:
                    new_dist = dist[node_idx] + edge.weight
                    if dist[edge.to] is None:
                        dist[edge.to] = new_dist
                    else:
                        dist[edge.to] = min(new_dist, dist[edge.to])

    return dist

def main():
    top_ordering = topsort(g)
    # print(top_ordering)
    dists = dag_shortest_path(g, 0, g.vertices) 
    print(dists)
main()
