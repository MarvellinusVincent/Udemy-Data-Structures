class Graph:
    def __init__(self):
        self.dic = {}
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.dic.keys() and vertex2 in self.dic.keys():
            self.dic[vertex1].append(vertex2)
            self.dic[vertex2].append(vertex1)
            return "Successful"
        return "There is no vertex in the graph"
    
    def BFS(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deque = queue.pop(0)
            print(deque)
            for adjacent in self.dic[deque]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    queue.append(adjacent)
