class Node():
    def __init__(self, data = None, left = None, right = None, father = None):
        self.left = left
        self.right = right
        self.father = father
        self.data = data # este é um campo generico, para guardar informacões satelites)

    # Getters (não utilizados por fim de simplificação)
    # O código usa acesso direto aos atributos do objeto
    def getInfo(self): return self.data
    def getLeft(self): return self.left
    def getRight(self): return self.right
    def getFather(self): return self.father

class BTree():
    def __init__(self) -> None:
        self.root = None

    def inserirEVerificar(self, num):
        if self.root == None:
            self.root = Node(num, None, None, None)
            return True

        else:
            no_atual = self.root # cursor

            # Laço para percorrer a árvore e alocar um novo nó
            while True:
                if num == no_atual.data:
                    return False
                elif num < no_atual.data:
                    if no_atual.left == None:
                        novo_no = Node(num, None, None, no_atual)
                        no_atual.left = novo_no
                        return True
                    else:
                        no_atual = no_atual.left
                elif num > no_atual.data:
                    if no_atual.right == None:
                        novo_no = Node(num, None, None, no_atual)
                        no_atual.right = novo_no
                        return True
                    else:
                        no_atual = no_atual.right

def sortList(array):
    tree = BTree()
    repetiu = False
    for n in array:
        resultado = tree.inserirEVerificar(n)
        if resultado:
            continue
        else:
            print(f"uma repetição ocorreu com o número {n}")
            repetiu = True
            break
    if not repetiu:
        print("Não há repetições nessa lista")

# Teste
if __name__ == "__main__":
    array = [2, 4, 10]
    sortList(array)