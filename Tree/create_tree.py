class Tree:
    def __init__(self, parent, children = []):
        self.parent = parent
        self.children = children
    
    def __str__(self, level = 0):
        ret = " " * level + str(self.parent) + "\n"
        for child in self.children:
            res += child.__str__(level + 1)
        return ret
    
    def addChild(self, Tree):
        self.children.append(Tree)