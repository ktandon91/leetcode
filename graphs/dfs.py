from graph import acyclic_graph, State
g = acyclic_graph()


def dfs(vertex):
    if vertex.state == State.visited:
        return
    print(f"Visiting vertex : {vertex.vertex}")
    vertex.state = State.visited
    neighbours = vertex.neighbours
    for neighbour in neighbours:
        dfs(g.vertices[neighbour])

if __name__ == "__main__":
    for vertex in g.vertices:
        dfs(g.vertices[vertex])
