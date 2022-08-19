class Graph:
    def __init__(self, dic = None):
        if self.dic is None:
            dic = {}
        self.dic = dic
    
    def bfs(self, start, end):
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                newpath = list(path)
                if adjacent in newpath:
                    continue
                newpath.append(adjacent)
                queue.append(newpath)
        return "No destination to end city"