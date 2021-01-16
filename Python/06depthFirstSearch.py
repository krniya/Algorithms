class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def addChild(self, name):
        self.children.append(Node(name))

    def depthfirstsearch(self, arr):
        arr.append(self.name)
        for child in self.children:
            child.depthfirstsearch(arr)
        return arr
        
nodeA = Node('A')
nodeA.addChild('B')
nodeA.addChild('C')
nodeA.children[1].addChild('D')


print(nodeA.depthfirstsearch([]))
