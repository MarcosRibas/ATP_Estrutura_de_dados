from noLista import NoL

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.freq = 0

    def inserirLista(self, elem):
        if self.cabeca:
            ponteiro = self.cabeca
            while(ponteiro.next):
                ponteiro = ponteiro.next
            ponteiro.next = NoL(elem)
        else:
            self.cabeca = NoL(elem)

    def __repr__(self):
        r = ""
        ponteiro = self.cabeca
        while(ponteiro):
            print(f'{ponteiro.dado}')
            ponteiro = ponteiro.next
        return r


    def buscaLista(self, elem):
        ponteiro = self.cabeca
        r = 0
        while(ponteiro):
            if ponteiro.dado == elem:
                self.freq += 1    
            ponteiro = ponteiro.next
        
        return self.freq

    
    def aumentar(self):
        self.freq += 1
        return self.freq