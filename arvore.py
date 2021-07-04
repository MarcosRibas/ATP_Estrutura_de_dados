from noArvore import NoArvore
from lista import ListaEncadeada

class Arvore:
    def __init__(self, dado = None, nodo = None):
        if nodo:
            self.raiz = nodo
        elif dado:
            nodo = NoArvore(dado) #criar o nó
            self.raiz = nodo
        else:
            self.raiz = None

    def __str__(self):        
        return str(NoArvore)

    def inserirArv(self, dado, lista):
        pai = None
        n = self.raiz
        lista.inserirLista(dado)
        while (n):
            pai = n
            x = str(n.dado)
            if dado < x:
                n = n.left
            else:
                n = n.right
        if pai is None:
            self.raiz = NoArvore(dado, lista)
        elif dado < pai.dado:
            pai.left = NoArvore(dado, lista)
        else:
            pai.right = NoArvore(dado, lista)


    def imprimirArv(self, nodo = None): # percurso de forma simétrica a partir da raiz
        if nodo is None:
            nodo = self.raiz
        if nodo.left: #se o nó não for vazio
            self.imprimirArv(nodo.left) #rodar a mesma função sobre quem esta a esquerda
        print(nodo, end=' ')        
        if nodo.right:
            self.imprimirArv(nodo.right)


    def posordem(self, nodo = None): #percurso de pós ordem
        if nodo is None:
            nodo = self.raiz
        if nodo.left: #se contém nó a esquerda
            self.posordem(nodo.left)
        if nodo.right:
            self.posordem(nodo.right)
        print(nodo)

    def busca(self, valor = None, nodo = None): #percurso de pós ordem
        s = "encontrado"
        n = 'Não encontrado'
        if nodo is None:
            nodo = self.raiz
        if nodo.left: #se contém nó a esquerda
            nodo.lista.buscaLista(valor)
            self.busca(nodo.left)
            if nodo.left.dado == valor:
                print('Encontrado')
                return s                
        if nodo.right:
            nodo.lista.buscaLista(valor)
            self.busca(nodo.right)
            if nodo.right.dado == valor:
                print('Encontrado')
                return s
        return n
        
    








