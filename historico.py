
class Historico:
    """Classe de objeto para modelar o histórico das páginas"""
    def __init__(self):
        self.__historico = []
    
    def topo(self):
        """Verfica o tamanho do histórico, retorna do histórico a página do topo, se ocorrer erro retorna o histórico como está"""
        try: 
            temp=len(self.__historico)
            return self.__historico[temp-1]
        except:
            return self.__historico

    def inserir(self,pagina):
        """Insere páginas no histórico"""
        self.__historico.append(pagina)
    
    def remover(self):
        """Remove páginas do histórico"""
        self.__historico.pop()
    
    
    def tamanho(self):
        """Retorna o tamanho do histórico"""
        return len(self.__historico)
    
    def __str__(self):
        """Concatena as páginas do histórico"""
        saida=''
        for i in range(len(self.__historico)):
            saida=saida + '{}'.format(self.__historico[i]) + ' ' + '>' + ' '
        # return self.__historico.__str__()
        return saida
    
    def get_historico(self):
        """Retorna o histórico das páginas acessadas"""
        return self.__historico

    def vazio(self):
        """Testa se o histórico está vazio"""
        teste=len(self.__historico)
        return teste==0
    
    def limpar(self):
        """Limpa o histórico"""
        return self.__historico.clear()
    
    def deletar(self):
        """Deleta o histórico"""
        del self.__historico
    
    def imprimir(self):
        """Imprime o histórico"""
        for i in self.__historico:
            print(i)
    