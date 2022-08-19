from collections import defaultdict
class Graph:
    def __init__(self, number):
        self.dic = defaultdict(list)
        self.number = number
    
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def topologicalsortuntil(self, v, visited, stack):
        visited.append(v)
        for i in self.dic[v]:
            if i not in visited:
                self.topologicalsortuntil(i, visited, stack)
        stack.insert(0, v)
    
    def toplogicalsort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topologicalsortuntil(k, visited, stack)
        print(stack)