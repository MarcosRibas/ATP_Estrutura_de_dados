from lista import ListaEncadeada


class NoArvore:
    def __init__(self, dado, lista):
        self.dado = dado
        self.lista = ListaEncadeada()
        self.left = None # referencia ao filho a equerda
        self.right = None # referencia ao filho a direita


    def __str__(self):
        return str(self.dado)

