graph_sample = {
    "a": ["c"],
    "b": ["c","e"],
    "c": ["a","b","d","e"],
    "d": ["c"],
    "e": ["c","b"],
    "f": [],
}

graph_sample_2 = {
    "a": ['b','c'],
    'b': ['d','e'],
    'c': ['f','g'],
    'd': [],
    'e': ['h','i','k'],
    'f': ['l','m'],
    'g': [],
    'h': [],
    'i': [],
    'k': [],
    'l': ['o','p'],
    'm': ['q','r'],
    'o': [],
    'p': [],
    'q': [],
    'r': [],    
}

class Graph:
    def __init__(self,graph_dict={}):
        self.graph_dict = graph_dict
    
    def vertices(self):
        """ Returns the vertices of a graph """
        return list(self.graph_dict.keys())
    
    def edges(self):
        """ Returns the edges of a graph """
        return self.generate_edges()
    
    def add_vertex(self,vertex):
        """ If  the vertex "vertex" is not in 
        self.graph_dict, a key "vertex" with an 
        empty list as a value is added to the dict
        Otherwise, nothing has to be done """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]
        self.add_vertex(vertex2)
    def generate_edges(self):
        """ A static method generating the edges of the graph 'graph' """

        edges = []
        for vertex in self.graph_dict:
            for neighbor in self.graph_dict[vertex]:
                if (neighbor,vertex) not in edges:
                    edges.append((vertex,neighbor))
        return edges
    
    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generate_edges():
            res += str(edge) + " "
        return res
    def DFS(self,vertex):
        visited = []
        for v in self.graph_dict[vertex]:
            if v not in visited:
                visited += [v] + self.DFS(v)
                print(visited)
        return visited

    def BFS(self,vertex):
        queue = self.graph_dict[vertex]
        visited = []
        while len(queue) != 0:
            for v in self.graph_dict[queue[0]]:
                if v not in visited:
                    queue.append(v) 
            visited.append(queue.pop(0))
            print(visited)
        return visited
    def bfs_shortest_path(self,start,goal):
        if start == goal:
            return [goal]
        queue = [start]
        visited = [start]
        while queue:
            vertex = queue.pop(0)
            for v in self.graph_dict[vertex]:
                if v not in visited:
                    queue.append(v)
                    visited.append(v)
                    if v == goal:
                        return self.bfs_shortest_path(start,vertex) + [v]                
        return "No solution"
g = Graph(graph_sample_2)
print(g)
print(g.bfs_shortest_path('a','l'))
g.add_edge('b','l')
print(g.bfs_shortest_path('a','l'))