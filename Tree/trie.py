class TrieNode:
    def __init__(self):
        self.children = {}
        self.endstring = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for i in word:
            char = i
            node = curr.children.get(char)
            if node == None:
                node = TrieNode()
                curr.children.update({char:node})
            curr = node
        curr.endstring = True
        print("successfully added")
    
    def search(self, word):
        curr = self.root
        for i in word:
            node = curr.children.get(i)
            if node == None:
                return False
            curr = node
        if curr.endstring == True:
            return True
        return False
    
def delete(root, word, index):
    char = word[index]
    curr = root.children.get(char)
    candelete = False
    if len(curr.children) > 1:
        delete(curr, word, index + 1)
        return False
    if index == len(word) - 1:
        if len(curr.children) >= 1:
            curr.endstring = False
            return False
        else:
            root.children.pop(char)
            return True
    if curr.endstring == True:
        delete(curr, word, index + 1)
        return False
    candelete = delete(curr, word, index + 1)
    if candelete == True:
        root.children.pop(char)
        return True
    else:
        return False