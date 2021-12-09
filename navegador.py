from pilha import Pilha
import re
from binarytree import *


class Navegador:
    """Classe Navegador, responsável por controlar as classes pilha e árvore.
    Possui parâmetro de entrada como sendo o nome do arquivo do banco de dados de páginas, uma string."""
    def __init__(self,nome_arquivo):
        self.__historico=Pilha()
        self.__nome_arquivo=nome_arquivo
        self.__sites=[]
        self.__arvores=[]
        try:
            self.captar_banco(nome_arquivo)
        except:
            with open(nome_arquivo,'w') as arquivo:  
                arquivo.close()
            self.captar_banco(nome_arquivo)
        
    def captar_banco(self,nome_arquivo):
        """ Captura páginas de um banco de dados txt e alimenta uma lista.
        Passar o parâmetro nome_arquivo, sendo o nome do arquivo txt do banco de dados, uma string. 
        Instancia árvores a partir de páginas.""" 
        with open(nome_arquivo) as arquivo:
            for i in arquivo:
                i=i.strip('\n')
                self.__arvores.append(BinaryTree(i))
                self.teste_filho(i)
                self.__sites.append(i)
                i=i.replace('/','.',4)
                with open(i+'.txt','w') as arquivo2:
                    arquivo2.write('\n<O conteudo da pagina '+i+' esta sendo exibido.>')
                arquivo2.close()
            arquivo.close()
    
    def pegar_filho_esq(self,url):
        """Seleciona filho esquerdo de uma árvore url.
        Para funcionar, basta passar uma string url."""
        for i in self.__arvores:
            if str(i.getRoot())==url:
                temp = i.downLeft()
                i.resetCursor()
                return temp


    def pegar_filho_dir(self,url):
        """Seleciona filho direito de uma árvore url.
        Para funcionar, basta passar uma string url."""
        for i in self.__arvores:
            if str(i.getRoot())==url:
                temp = i.downRight()
                i.resetCursor()
                return temp

    """Testa se a nova_url de entrada é subpágina de alguma das páginas instanciadas.
    Caso seja, é alocada abaixo. Como parâmetro é passado uma nova_url."""
    def teste_filho(self,nova_url):
        for i in self.__arvores:
            nomeFilho=i.getRoot()
            if str(nomeFilho) in str(nova_url) and str(nomeFilho) != str(nova_url) and (len(nova_url.split('/'))) == (len(str(nomeFilho).split('/'))+1) :
                if i.downLeft() is None:
                    i.resetCursor()
                    i.addLeftChild(nova_url)
                    i.resetCursor()
                elif i.downRight() is None:
                    i.resetCursor()
                    i.addRightChild(nova_url)
                    i.resetCursor()
                else:
                    pass
            
    def adicionar(self,nova_url):
        """Método para adicionar uma nova_url. Testa existência no banco de dados.
        Testa se a página é subpágina. Instancia a árvore da página. Escreve mensagem a ser
        renderizada da página nova. O parâmetro passado é nova_url, uma string."""
        if not self.existencia(nova_url):
            with open(self.__nome_arquivo,'a') as arquivo:
              arquivo.write('\n'+nova_url)
              self.__sites.append(nova_url)
              self.__arvores.append(BinaryTree(nova_url))
              self.teste_filho(nova_url)
            #   self.__sites.append(nova_url)
              with open(nova_url.replace('/','.',4)+'.txt','w') as arquivo2:
                  arquivo2.write('\n<O conteudo da pagina '+nova_url+' esta sendo exibido.>')
              arquivo2.close()
              arquivo.close()    
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

        

