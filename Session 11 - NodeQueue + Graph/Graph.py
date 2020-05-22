graph_sample = {
    "a": ["c"],
    "b": ["c","e"],
    "c": ["a","b","d","e"],
    "d": ["c"],
    "e": ["c","b"],
    "f": [],
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

    def first_acquaintance(self,vertex,visited_vertices):
        for v in self.graph_dict[vertex]:
            if v not in visited_vertices:
                return v
        return None

    ''' Return a list of all possible destinations from a vertex '''
    def recursive_func(self,vertex,visited_vertices): 
        while self.first_acquaintance(vertex,visited_vertices) != None:
            new_vertex = self.first_acquaintance(vertex,visited_vertices)
            visited_vertices.append(new_vertex)
            visited_vertices = self.recursive_func(new_vertex,visited_vertices)
        return visited_vertices
        
    def possible_destinations(self,vertex):
        return self.recursive_func(vertex,[vertex])
   
g = Graph(graph_sample)
print(g)
print(g.possible_destinations('d'))
# g.add_vertex("a")
# g.add_edge('b','a')
# g.add_vertex('c')
# g.add_edge('d','f')

# print(g)
