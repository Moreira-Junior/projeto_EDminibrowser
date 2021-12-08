class Node:
    def __init__(self, dado):
        self.__dado = dado
        self.__filhoEsq = None
        self.__filhoDir = None

    def inserirEsq(self, dado):
        if self.__filhoEsq == None:
            self.__filhoEsq = Node(dado)

    def inserirDir(self, dado):
        if self.__filhoDir == None:
            self.__filhoDir = Node(dado)

    def getFilhoEsq(self):
        return self.__filhoEsq

    def getFilhoDir(self):
        return self.__filhoDir

    def setValor(self, novoValor):
        self.__dado = novoValor

    def getValor(self):
        return self.__dado

    def temFilhoEsq(self):
        return self.__filhoEsq != None

    def temFilhoDir(self):
        return self.__filhoDir != None

    def __str__(self):
        return str(self.__dado)
