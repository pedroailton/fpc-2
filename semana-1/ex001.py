class Node():
    def __init__(self, data = None, left = None, right = None, father = None):
        self.left = left
        self.right = right
        self.father = father
        self.data = data # este é um campo generico, para guardar informacões satelites)

    # Getters
    def getInfo(self): return self.data
    def getLeft(self): return self.left
    def getRight(self): return self.right
    def getFather(self): return self.father

class BTree():
    def __init__(self) -> None:
        self.root = None

    def maximum(self, node: Node) -> Node:
        if node == None:
            return None
        atual = node
        while atual.getRight() is not None:
            atual = atual.getRight()
        return atual

    def minimum(self, node : Node) -> Node:
        if node == None:
            return None
        atual = node
        while atual.getLeft() is not None:
            atual = atual.getLeft()
        return atual

    def sucessor(self, node: Node) -> Node:
        if node == None:
            return
        node.getRight()
        return

    def predecessor(self, node: Node) -> Node:
        if node == None:
            return
        node.getLeft()
        return

    def insert(self, node: Node) -> None:
        # Se a árvore estiver vazia
        if self.root == None:
            self.root = node

        