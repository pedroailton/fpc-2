class BTree () {
    function constructor(
        nodes = [];
    ) {}
   // o que deve estar em um constructor e o que deve estar fora dele? 

    // Retorna informações do nó p da árvore
    function getInfo(p) {
        return self.data;
    }
    function getLeft(p) {
        return self.left
    }

    function getRight(p) {
        return self.right
    }

    function getFather(p) {
        return self.father
    }
}

class Node() {
    function constructor() {
    }
}

// Criando uma árvore

const input = [1, 2, 3, 4]