class Node():
    def __init__(self, key = None, left = None, right = None, father = None):
        self.left = left
        self.right = right
        self.father = father
        self.key = key

class BTree():
    def __init__(self) -> None:
        self.root = None

    def maximum(self, node: Node) -> Node:
        no_atual = node
        while no_atual.right is not None:
            no_atual = no_atual.right
        return no_atual

    def minimum(self, node: Node) -> Node:
        no_atual = node
        while no_atual.left is not None:
            no_atual = no_atual.left
        return no_atual

    def sucessor(self, x: Node) -> Node:
        if x.right:
            return self.minimum(x.right)
        y = x.father
        while y and x == y.right:
            x = y
            y = y.father
        return y

    def predecessor(self, x: Node) -> Node:
        if x.left:
            return self.minimum(x.left)
        y = x.father
        while y and x == y.left:
            x = y
            y = y.father
        return y

    def insert(self, z: Node) -> None:
        y = None
        x = self.root

        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.father = y
        if not y:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else: 
            y.right = z

    def delete(self, z: Node) -> Node:
        w = None # Adicionei ela para uma simplificação no final
        x = None
        y = None

        if not z.left or not z.right:
            y = z
        else:
            y = self.sucessor(z)

        if y.left != None:
            x = y.left
        else:
            x = y.right

        if x != None:
            x.father = y.father

        w = y.father
        if w == None:
            self.root = x
        else:
            if y == w.left:
                w.left = x
            else:
                w.right = x

        if y != None:
            z.key = y.key

        return y

def testar_arvore():
    tree = BTree()
    
    # Valores baseados na árvore de exemplo da operação Delete do material
    chaves = [15, 5, 16, 3, 12, 20, 10, 13, 18, 23, 6, 7] 
    
    print("--- 1. Testando Inserção (Insert) ---")
    for chave in chaves:
        tree.insert(Node(chave))
    print(f"Chaves inseridas: {chaves}")
    
    # Função auxiliar baseada no INORDER-TREE-WALK do material
    # Exibe os números em ordem crescente se a árvore estiver correta
    def imprimir_em_ordem(node):
        if node is not None:
            imprimir_em_ordem(node.left)
            print(node.key, end=" ")
            imprimir_em_ordem(node.right)
            
    print("\n--- 2. Percurso em Ordem ---")
    print("Resultado esperado: 3 5 6 7 10 12 13 15 16 18 20 23")
    print("Resultado obtido:   ", end="")
    imprimir_em_ordem(tree.root)
    print("\n")
    
    print("--- 3. Testando Mínimo e Máximo ---")
    min_node = tree.minimum(tree.root)
    max_node = tree.maximum(tree.root)
    print(f"Mínimo: {min_node.key if min_node else None} (Esperado: 3)")
    print(f"Máximo: {max_node.key if max_node else None} (Esperado: 23)\n")
    
    # Função auxiliar de busca (Search) para resgatar os objetos Node para os testes seguintes
    def buscar(node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return buscar(node.left, key)
        return buscar(node.right, key)
    
    print("--- 4. Testando Sucessor e Predecessor ---")
    alvo = buscar(tree.root, 15) # Raiz
    suc = tree.sucessor(alvo)
    pred = tree.predecessor(alvo)
    print(f"Analisando o nó ({alvo.key}):")
    print(f"Sucessor: {suc.key if suc else None} (Esperado: 16)")
    print(f"Predecessor: {pred.key if pred else None} (Esperado: 13)\n")
    
    print("--- 5. Testando Deleção (Delete) ---")
    chave_deletar = 16
    alvo_delete = buscar(tree.root, chave_deletar)
    print(f"Deletando o nó {alvo_delete.key}...")
    tree.delete(alvo_delete)
    
    print("\nPercurso em Ordem após a deleção (não deve conter o 16):")
    imprimir_em_ordem(tree.root)
    print()

if __name__ == "__main__":
    testar_arvore()