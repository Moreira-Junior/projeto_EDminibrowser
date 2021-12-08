from pilha import Pilha
from arvorebinaria import *
import re

class Navegador:
    def __init__(self,nome_arquivo):
        self.__historico=Pilha()
        self.__home=''
        self.__nome_arquivo=nome_arquivo
        self.__sites=[]
        self.__arvores=[]
        self.captar_banco(nome_arquivo)
        
    def captar_banco(self,nome_arquivo):
        """ = """ 
        with open(nome_arquivo) as arquivo:
            for i in arquivo:
                i=i.strip('\n')
                self.__arvores.append(ArvoreBinaria(i))
                self.teste_filho(i)
                self.__sites.append(i)
                i=i.replace('/','.',4)
                with open(i+'.txt','w') as arquivo2:
                    arquivo2.write('\n<O conteudo da pagina '+i+' esta sendo exibido.>')
            arquivo2.close()
            arquivo.close()
    
    def pegar_filho_esq(self,url):
        for i in self.__arvores:
            if str(i.getRaiz())==url:
                temp = i.getBaixoEsq()
                i.resetCursor()
                return temp


    def pegar_filho_dir(self,url):
        for i in self.__arvores:
            if str(i.getRaiz())==url:
                temp = i.getBaixoDir()
                i.resetCursor()
                return temp

    def teste_filho(self,nova_url):
        for i in self.__arvores:
            if str(i.getRaiz()) in str(nova_url) and str(i.getRaiz()) != str(nova_url) and (len(nova_url.split('/'))) == (len(str(i.getRaiz()).split('/'))+1) :
                if i.getBaixoEsq() is None:
                    i.resetCursor()
                    i.addFilhoEsq(nova_url)
                    i.resetCursor()
                elif i.getBaixoDir() is None:
                    i.resetCursor()
                    i.addFilhoDir(nova_url)
                    i.resetCursor()
                else:
                    pass
          
    def adicionar(self,nova_url):

        
        if not self.existencia(nova_url):
            with open(self.__nome_arquivo,'a') as arquivo:
              arquivo.write('\n'+nova_url)
              self.__sites.append(nova_url)
              self.__arvores.append(ArvoreBinaria(nova_url))
              self.teste_filho(nova_url)
              self.__sites.append(nova_url)
              with open(nova_url+'.txt','w') as arquivo2:
                  arquivo2.write('\n<O conteudo da pagina '+nova_url+' esta sendo exibido.>')
              arquivo2.close()
              arquivo.close()    
        return self.existe

    def empilhar(self,url):
        self.__historico.empilha(url)
    
    def mostra_historico(self):
        try:
            return self.__historico.imprimir()
        except:
            return ''


    def voltar(self):
        if self.__historico.tamanho()<1:
            self.__historico=[]
        else:
            self.__historico.desempilha()
    
    def pilha_vazia(self):
        return self.__historico.estaVazia()
    
    def existencia(self,nova_url):
        self.existe=False
        for i in self.__sites:
            if i==str(nova_url):
                self.existe=True
        return self.existe
    
    def topo_pilha(self):
        return self.__historico.topo()

    def tamanho(self):
        return self.__historico.tamanho()
    
    def forma(self,nova_url):
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
        with open(url+'.txt','r') as arquivo2:
            string=arquivo2.read()
        arquivo2.close()
        return string

        

