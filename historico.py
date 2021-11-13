
class Historico:
    def __init__(self):
        self.__historico = []
    
    def topo(self):
        try: 
            temp=len(self.__historico)
            return self.__historico[temp-1]
        except:
            return self.__historico

    def inserir(self,pagina):
        self.__historico.append(pagina)
    
    def remover(self):
        self.__historico.pop()
    
    
    def tamanho(self):
        return len(self.__historico)
    
    def __str__(self):
        saida=''
        for i in range(len(self.__historico)):
            saida=saida + '{}'.format(self.__historico[i]) + ' ' + '>' + ' '
        # return self.__historico.__str__()
        return saida
    
    def get_historico(self):
        return self.__historico

    def vazio(self):
        teste=len(self.__historico)
        return teste==0
    
    def limpar(self):
        return self.__historico.clear()
    
    def deletar(self):
        del self.__historico
    
    def imprimir(self):
        for i in self.__historico:
            print(i)
    