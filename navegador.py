from pilha import Pilha
import re

class Navegador:
    def __init__(self,nome_arquivo):
        self.__historico=Pilha()
        self.__home=''
        self.__nome_arquivo=nome_arquivo
        self.__sites=[]
        self.captar_banco(nome_arquivo)
        
    def captar_banco(self,nome_arquivo):
        """ = """ 
        with open(nome_arquivo) as arquivo:
            for i in arquivo:
                i=i.strip('\n')
                self.__sites.append(i)
          
    def adicionar(self,nova_url):
        
        if not self.existencia(nova_url):
            with open(self.__nome_arquivo,'a') as arquivo:
              arquivo.write('\n'+nova_url)
              self.__sites.append(nova_url)
              arquivo.close()
              
        return self.existe
    
    def home(self,url):
        self.__home=url
        return self.__home

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
            # i=i.strip('\n')
            if i==str(nova_url):#.strip('\n'):
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
        elif nova_url[0:5]=='https':
            testeForma = re.findall('https://[a-z0-9_.\-]+\.[a-z0-9_\-/]+',nova_url)  
        else:
            testeForma = re.findall('www.[a-z0-9_.\-]+\.[a-z0-9_\-/]+',nova_url)
        if testeForma==[]:
            self.formato=False
        else:
            self.formato=True
        return self.formato

    def imprime_historico(self):
        # """Imprime o histórico"""
        # print(self.__historico)
        # for i in self.__historico:
        #     print(i)
        return self.__historico.imprime_historico()
    
        


      #método para avaliar se a forma da url que será adicionada é válida
    #   self.__forma = self.__novaurl.split('.')
    #   self.__testf=True
    #   if self.__forma[0]=='\nwww':
    #       if self.__forma[-1]=='com' or self.__forma[-1]=='br' or self.__forma[-1]=='net':
    #           self.__testf=True
    #       else:
    #           self.__testf=False
    #   else:
    #       self.__testf=False
    #   return self.__testf 
        

