class Graph:
    def __init__(self):
        self.dic = {}
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.dic.keys() and vertex2 in self.dic.keys():
            self.dic[vertex1].append(vertex2)
            self.dic[vertex2].append(vertex1)
            return "Successful"
        return "There is no vertex in the graph"
    
    def DFS(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            pop = stack.pop()
            print(pop)
            for adjacent in self.dic[pop]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    stack.append(adjacent)