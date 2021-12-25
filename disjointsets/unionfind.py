class DisjointSet:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.parent = {}
        # Initialize parent of vertex as vertex itself 
        for v in vertices:
            self.parent[v] = v
        # Default rank of 0 for each vertex in 
        self.rank = dict.fromkeys(vertices, 0)
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] > self.rank[yroot]:
            self.rank[yroot] = xroot
        elif self.rank[yroot] > self.rank[xroot]:
            self.rank[xroot] = yroot
        else:
            self.rank[yroot] = xroot
            self.rank[xroot]+=1

ds = DisjointSet()

