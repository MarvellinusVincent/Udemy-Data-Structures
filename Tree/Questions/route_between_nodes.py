class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def bfs(self, start, end):
        visited = [start]
        queue = [start]
        path = False
        while queue:
            path = queue.pop(0)
            for adjacent in self.gdict[path]:
                if adjacent not in visited:
                    if adjacent == end:
                        return True
                    else:
                        visited.append(adjacent)
                        queue.append(adjacent)
        return "No destination to end city"
            

customDict = { "a" : ["c","d", "b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : ["a"],
            "e" : ["f", "a"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }
g = Graph(customDict)
print(g.bfs("a", "h"))