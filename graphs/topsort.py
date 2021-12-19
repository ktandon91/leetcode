# 1. Pick an unvisited node
# 2. Beginning the start node, do a dfs only visiting the unvisited node
# 3. During recursive callback of the DFS, add the current node the 
#    topolofical ordering in reverse order.
# **TopSort is same as pre-order in tree. However, for graphs that's not the case.
# **REVERSE OF POST ORDER TRAVERSAL IS TOPSORT 

#TODO : remove pre_order part as it is just for comparison
from graph import acyclic_graph_from_graph_list

g = acyclic_graph_from_graph_list()

# post_order = []
def dfs(at, visited, visited_nodes, graph):
    visited[at] = True
    neighbours = graph.adjacency_list[at]

    for neighbour in neighbours:
        if not visited[neighbour]:
            dfs(neighbour, visited, visited_nodes, graph)
    # post_order.append(at)
    visited_nodes.append(at)

def topsort(graph):
    N = g.vertices
    top_ordering = [0 for _ in range(N)] 
    visited = [False for _ in range(N)]
    i = N-1 # Index for maintaining topological ordering
    for at in range(g.vertices):
        if not visited[at]:
            visited_nodes = []
            dfs(at, visited, visited_nodes, graph)
            for node in visited_nodes:
                top_ordering[i] = node
                i-=1
    return top_ordering 

# if __name__ == "__main__":
#     print(topsort(g))
    # post_order.reverse()
    # print(post_order)


