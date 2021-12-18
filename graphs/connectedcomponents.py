from graph import connected_component, State
g = connected_component()


def dfs(vertex, count):
    if vertex.state == State.visited:
        return
    vertex.state = State.visited
    vertex.connected_component = count
    print(f"Visiting vertex : {vertex.vertex}, connected to group - {vertex.connected_component} ")
    neighbours = vertex.neighbours
    for neighbour in neighbours:
        dfs(g.vertices[neighbour], count)

if __name__ == "__main__":
    count=0
    for vertex in g.vertices:
        v = g.vertices[vertex]
        if v.state != State.visited:
            count+=1
            dfs(g.vertices[vertex], count)
