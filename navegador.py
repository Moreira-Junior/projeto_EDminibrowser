from pilha import Pilha
import re
from Grafo import Grafo

class Navegador:
    """Classe Navegador, responsável por controlar as classes pilha e grafo.
    Possui parâmetro de entrada como sendo o nome do arquivo do banco de dados de páginas, uma string."""
    def __init__(self,nome_arquivo):
        self.__historico=Pilha()
        self.__nome_arquivo=nome_arquivo
        self.__sites=[] 
        self.__grafo = Grafo()
        self.__vertices=self.__grafo.getListVert()
        self.__raiz=self.__grafo.addVertice('/')
        try:
            self.captar_banco(nome_arquivo)
        except:
            with open(nome_arquivo,'w') as arquivo:  
                arquivo.write('''www.google.com
www.facebook.com
www.ifpb.edu.br
www.ifpb.edu.br/tsi
www.ifpb.edu.br/rc
www.ufpb.br
www.instagram.com
www.ifpb.edu.br/tsi/professores''')
                arquivo.close()
            self.captar_banco(nome_arquivo)
        
    def captar_banco(self,nome_arquivo):
        """ Captura páginas de um banco de dados txt e alimenta uma lista.
        Passar o parâmetro nome_arquivo, sendo o nome do arquivo txt do banco de dados, uma string. 
        Instancia vértices do grafo a partir de páginas.""" 
        with open(nome_arquivo) as arquivo:
            for i in arquivo:
                i=i.strip('\n')
                self.__grafo.addVertice(i)
                self.__sites.append(i)
                i=i.replace('/','.',4)
                with open(i+'.txt','w') as arquivo2:
                    arquivo2.write('\n<O conteudo da pagina '+i+' esta sendo exibido.>')
                arquivo2.close()
            arquivo.close()

        for i in self.__vertices:
            self.teste_filho(i)
            if not '/' in str(i):
                self.__grafo.addAresta(self.__raiz,i)
    
    
    def teste_filho(self,nova_url):
        """Testa se a nova_url de entrada é subpágina de alguma das páginas instanciadas.
        Caso seja, é alocada abaixo. Como parâmetro é passado uma nova_url."""
        for i in self.__vertices:
            nomeFilho=i
            if str(nomeFilho) in str(nova_url) and str(nomeFilho) != str(nova_url) and (len(str(nova_url).split('/'))) == (len(str(nomeFilho).split('/'))+1) and str(nomeFilho)!='/':
                self.__grafo.addAresta(nomeFilho,nova_url)

            
    def adicionar(self,nova_url):
        """Método para adicionar uma nova_url. Testa existência no banco de dados.
        Testa se a página é subpágina. Instancia o vértice da página. Escreve mensagem a ser
        renderizada da página nova. O parâmetro passado é nova_url, uma string."""
        if not self.existencia(nova_url):
            with open(self.__nome_arquivo,'a') as arquivo:
              arquivo.write('\n'+nova_url)
              self.__sites.append(nova_url)
              obj=self.__grafo.addVertice(nova_url)
              self.teste_filho(obj)
              with open(nova_url.replace('/','.',4)+'.txt','w') as arquivo2:
                  arquivo2.write('\n<O conteudo da pagina '+nova_url+' esta sendo exibido.>')
              arquivo2.close()
              arquivo.close()
              if not '/' in str(obj):
                self.__grafo.addAresta(self.__raiz,obj)    
        return self.existe

    def empilhar(self,url):
        """Manipula a pilha histórico, empilhando uma url."""
        self.__historico.empilha(url)
    
    def mostra_historico(self):
        """Manipula a pilha histórico, imprimindo seu conteúdo."""
        try:
            return self.__historico.imprimir()
        except:
            return ''

    """Manipula a pilha histórico, desempilhando o elemento do topo."""
    def voltar(self):
        if self.__historico.tamanho()<1:
            self.__historico=[]
        else:
            self.__historico.desempilha()
    
    def pilha_vazia(self):
        """Verifica se a pilha está vazia."""
        return self.__historico.estaVazia()
    
    def existencia(self,nova_url):
        """Verifica se uma página existe na lista de sites. Para funcionar
        bastar passar o parâmetro nova_url."""
        self.existe=False
        for i in self.__sites:
            if i==str(nova_url):
                self.existe=True
        return self.existe
    
    def topo_pilha(self):
        """Manipula a pilha histórico, retornando seu elemento de topo."""
        return self.__historico.topo()

    def tamanho(self):
        """Manipula a pilha histórico, retornando seu tamanho."""
        return self.__historico.tamanho()
    
    def forma(self,nova_url):
        """Testa forma da nova_url passada. Fazendo verificação com expressões regulares."""
        self.formato=True
        if nova_url[0:4]=='http':
            testeForma = re.findall('http://[a-z0-9_.\-]+\.[a-z0-9_\-/]+',nova_url) 
        else:
            testeForma = re.findall('www.[a-z0-9_.\-]+\.[a-z0-9_\-/]+',nova_url)
        if testeForma==[]:
            self.formato=False
        else:
            self.formato=True
        return self.formato

    def renderizar(self,url):
        """Responsável por ler o conteúdo da página passada como parâmetro e devolver seu conteúdo
        para impressão."""
        with open(url+'.txt','r') as arquivo2:
            string=arquivo2.read()
        arquivo2.close()
        return string
    
    def print_adjacentes(self,url):
        '''Responsável por imprimir os vértices adjacentes ao vértice url.'''
        return self.__grafo.printAdj(url)
    
    def printGrafo(self):
        '''Responsável por imprimir o grafo com seus vértices e arestas.'''
        print(self.__grafo)

    def match(self,nova_url):
        '''Responsável por verificar se a url inserida possui páginas superiores.'''
        return self.__grafo.match(nova_url)



        
    


        

