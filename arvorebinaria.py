from node import *

class ArvoreBinaria:
    def __init__(self, dado_raiz):
        self.__raiz = Node(dado_raiz)
        self.__cursor = self.__raiz

    def getRaiz(self):
        return self.__raiz

    def getBaixoEsq(self):
        if self.__cursor.temFilhoEsq():
            self.__cursor = self.__cursor.getFilhoEsq()
            return self.__cursor
        return None

    def getBaixoDir(self):
        if self.__cursor.temFilhoDir():
            self.__cursor = self.__cursor.getFilhoDir()
            return self.__cursor
        return None

    def addFilhoEsq(self, dado):
        if not self.__cursor.temFilhoEsq():
            self.__cursor.inserirEsq(dado)

    def addFilhoDir(self, dado):
        if not self.__cursor.temFilhoDir():
            self.__cursor.inserirDir(dado)

    def resetCursor(self):
        self.__cursor = self.__raiz

    def getCursor(self):
        return self.__cursor

    def busca(self, chave):
        return self.__buscaDado(chave, self.__raiz)

    def __buscaDado(self, chave, node):
        if node == None:
            return False
        if chave == node.getValor():
            return True
        elif self.__buscaDado(chave, node.getFilhoEsq()):
            return True
        else:
            return self.__buscaDado(chave, node.getFilhoDir())

    def preOrdem(self):
        self.__preOrdem(self.__raiz)

    def inOrdem(self):
        self.__inOrdem(self.__raiz)

    def posOrdem(self):
        self.__posOrdem(self.__raiz)    

    def __preOrdem(self, node):
        if node == None:
            return None
        print(f'{node.getValor()}', end='')
        self.__preOrdem(node.getFilhoEsq())
        self.__preOrdem(node.getFilhoDir())
    
    def __inOrdem(self, node):
        if node == None:
            return None
        self.__inOrdem(node.getFilhoEsq())
        print(f'{node.getValor()}', end='')
        self.__inOrdem(node.getFilhoDir())
    
    def __posOrdem(self, node):
        if node == None:
            return None
        self.__posOrdem(node.getFilhoEsq())
        self.__posOrdem(node.getFilhoDir())
        print(f'{node.getValor()}', end='')

    def deletaArvore(self):
        self.__raiz = None

    def deletaNode(self, chave):
        self.__deletaNode(self.__cursor, chave)

    def __deletaNode(self, raiz, chave):
        if raiz is None:
            return None
        elif raiz.getFilhoEsq() == None and raiz.getFilhoDir == None:
            return None

        if raiz.getFilhoEsq() == None:
            if raiz.getFilhoDir().getValor() == chave:
                raiz.setFilhoDir(None)
        elif raiz.getFilhoDir() == None:
            if raiz.getFilhoEsq().getValor() == chave:
                raiz.setFilhoEsq(None)        

