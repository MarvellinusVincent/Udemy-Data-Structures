import heapq
class Edge:
    def __init__(self, node, start, target):
        self.node = node
        self.start = start
        self.target = target

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")
    
    def __lt__(self, other):
        return self.min_distance < other.min_distance
    
    def add_edge(self, node, destination):
        edge = Edge(node, self, destination)
        self.neighbors.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap = []
    
    def calculate(self, start):
        start.min_distance = 0
        heapq.heappush(self.heap, start)
        while self.heap:
            vertex = heapq.heappop(self.heap)
            if vertex.visited:
                continue
            for edge in vertex.neighbors:
                start = edge.vertex
                target = edge.target
                new_distance = start.min_distance + edge.node
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    heapq.heappush(self.heap, target)
            vertex.visited = True
    
    def get_shortest_path(self, vertex):
        print(f"The shortest path to the vertex is: {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end = " ")
            actual_vertex = actual_vertex.predecessor

from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def dijkstra(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    return visited, path

customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

print(dijkstra(customGraph, "A"))



