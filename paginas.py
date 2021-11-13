
class Pagina:
    def __init__ (self,url):
        self.__url=url
        
    def get_url(self):
        return self.__url

    def __str__(self):
        return f'{self.__url}'
    
    def deletar(self):
        self.__url
    
    def teste(self):
        pass
    
    def ler_arquivo(self,nome_arquivo):
      with open(nome_arquivo) as arquivo:
        self.__sites=[]
        self.__cont=0
        self.__teste=True
        for i in arquivo:
          i=i.strip('\n')
          self.__sites.append(i)

        for i in self.__sites:
          if i==self.__url:
            self.__cont+=1

        if self.__cont>=1:
          print('Página encontrada!')
        else:
          print('Página não encontrada!')
          self.__teste=False
        
        return self.__teste
    
          
  