from ElementosGrafo import *

class Grafo():

    def __init__(self):
        self.__vertices = list()
        self.__arestas = list()
    
    def addListVer(self,url):
        self.__vertices.append(url)
    
    def getListVert(self):
        return self.__vertices

    def addVertice(self, nome)->Vertice:
        v = Vertice(nome)
        self.__vertices.append(v)
        return v

    def addAresta(self, origem: Vertice, destino: Vertice)->Aresta:
        e = Aresta(origem, destino)
        origem.addAdj(e)
        self.__arestas.append(e)
        return e

    def __str__(self):
        r = ''
        for u in self.__vertices:
            if len(u.adj) == 0:
                continue
            r += (str(u.dado) + ' -> ')
            for e  in u.adj:
                v: Vertice = e.destino
                r += v.dado + ', '
            r += '\n'
        return r

    def getNumVertices(self):
        return len(self.__vertices)

    def printAdj(self,origem):
        for i in self.__vertices:
            if str(i)==origem:
                print(i.printAdjs())
        

    def getNumArestas(self):
        return len(self.__arestas)	
    
    def match(self,nova_url):
        '''Responsável por verificar se a url inserida possui páginas superiores.'''
        self.testeMatch=False 
        for i in self.__vertices:
            nomeFilho=str(i)
            if (nomeFilho) in (nova_url) and (nomeFilho) != (nova_url) and (len((nova_url).split('/'))) == (len((nomeFilho).split('/'))+1) and nomeFilho!='/':
                self.testeMatch=True
                self.match(nomeFilho)
                break
            elif len(str(nova_url).split('/'))==1 and nomeFilho!='/':
                self.testeMatch=True
                break
        return self.testeMatch

                
        
            
        

            






