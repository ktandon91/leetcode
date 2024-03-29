from enum import Enum
from collections import namedtuple

Edge = namedtuple("Edge", "to weight")
class State(Enum):
    unvisited, visited, visiting = 1, 2, 3

class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.neighbours = {} #key will be vertex_name , value will be weight
        self.state = State.unvisited

    def __str__(self):
        return f"Node:{self.vertex} with neighbours:{self.neighbours}"

class GraphDict:
    def __init__(self):
        self.vertices = {}
        self.count = 0
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex)
        else:
            raise Exception("Vertex Already Exists")
        self.count+=1
        return self.vertices[vertex]
    
    def add_edge(self, src, dest, weight=0): #Default for unweighted graphs  
        if src not in self.vertices:
            self.add_vertex(src)
        if dest not in self.vertices:
            self.add_vertex(dest)
        src = self.vertices[src]
        src.neighbours[dest]=weight

    def __str__(self):
        g = f"Total Vertices: {self.count}\n"
        for vertex in self.vertices:
            g=g+f"{self.vertices[vertex]}\n"
        return g



# Class representing a simple graph using an edge list converted to adjacency list
class GraphList:
    # Basic constructor method
    def __init__(self, num_of_nodes, edge_list=[]):
        # Convert edge list to adjacency list,
        # represented with a multi-dimensional array
        self.adjacency_list = [[] for _ in range(num_of_nodes)]
        self.vertices = num_of_nodes
        
        # Add edges to corresponding nodes of the graph
        if edge_list:
            for (origin, dest) in edge_list:
                self.adjacency_list[origin].append(dest)

    def add_edge(self, src, destination):
        self.adjacency_list[src].append(destination)

    def __str__(self):
        g_view = ""
        for origin in range(len(self.adjacency_list)):
        # print current vertex and all its neighboring vertices
            for dest in self.adjacency_list[origin]:
                g_view=g_view+ f'{origin} —> {dest} '
            g_view=g_view+'\n'
        return g_view   
 
class GraphListTuple:
    def __init__(self, vertices, edge_list=[]):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(self.vertices)]

        if edge_list:
            for origin, des, distance in edge_list:
                edge = Edge(des, distance)
                self.adjacency_list[origin].append(edge)

    # def add_edge(self, src, destination, weight):
    #     self.adjacency_list[src].append({destination:weight})

    def __str__(self):
        g_view = ""
        for origin in range(len(self.adjacency_list)):
        # print current vertex and all its neighboring vertices
            for edge in self.adjacency_list[origin]:
                g_view=g_view+ f'{origin} ---{edge.weight}--—> {edge.to} '
            g_view=g_view+'\n'
        return g_view  
    

def acyclic_graph():
    g = GraphDict()
    #       A
    #     /    \
    #    B      C
    #  /   \    /
    # D    E   F
    g.add_edge('A', 'B', 3)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'D', 3)
    g.add_edge('B', 'E', 3)
    g.add_edge('C', 'F', 3)

    return g

def acyclic_graph_from_graph_list():
    #       0
    #     /    \
    #    1      2
    #  /   \    /
    # 3    4   5
    edge_list = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    num_of_nodes = 6
    graph = GraphList(num_of_nodes, edge_list) 
    return graph

def connected_component():
    g = GraphDict()
    #       A
    #     /    \
    #    B      C
    #  /   \    /
    # D    E   F
    g.add_edge('A', 'B', 3)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'D', 3)
    g.add_edge('B', 'E', 3)
    g.add_edge('C', 'F', 3)
    g.add_edge('G', 'G', 0)
    g.add_edge('H', 'H', 0)
    return g

 
def graph_bfs():
    # Set up an edge list and number of nodes
    edge_list = [(0, 1), (1, 2), (2, 3), (0, 2), (3, 2), (4, 5), (5, 4)]
    num_of_nodes = 6
 
    graph = GraphList(num_of_nodes, edge_list) 
    graph.add_edge(3,4)
    return graph

def single_source_shortest_path():
    edge_list = [(0,1,3), (0,2,2), (0,5,3), (1,3,1), (1,2,6), (2,3,1),
                 (2,4,10), (3,4,5), (5,4,7)]

    num_of_nodes = 7
    g = GraphListTuple(num_of_nodes, edge_list)
    return g

# print(single_source_shortest_path())
