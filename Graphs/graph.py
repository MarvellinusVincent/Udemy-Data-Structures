class Graph:
    def __init__(self):
        self.dic = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.dic.keys():
            self.dic[vertex] = []
            return "Successful"
        return "There is a duplicate"
    
    def print_graph(self):
        for vertex in self.dic:
            print (vertex, ":", self.dic[vertex])
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.dic.keys() and vertex2 in self.dic.keys():
            self.dic[vertex1].append(vertex2)
            self.dic[vertex2].append(vertex1)
            return "Successful"
        return "There is no vertex in the graph"
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.dic.keys() and vertex2 in self.dic.keys():
            try:
                self.list[vertex1].remove(vertex2)
                self.list[vertex2].remove(vertex1)
            except:
                return "Error found"
            return "Successful"
        return "There is no vertex in the graph"
    
    def remove_vertex(self, vertex):
        if vertex in self.dic.keys():
            for edge in self.dic[vertex]:
                self.dic[edge].remove(vertex)
            del self.dic[vertex]
            return "Successful"
        return "There is no vertex in the graph"