
class Pagina:
    """Classe do objeto página"""
    def __init__ (self,url):
        """Construtor da url"""
        self.__url=url
        
    def get_url(self):
        """Retorna a url"""
        return self.__url

    def __str__(self):
        """Retorna o objeto url"""
        return f'{self.__url}'
    
    def deletar(self):
        """Deleta a url"""
        self.__url
    
    def teste(self):
        pass
    
    def ler_arquivo(self,nome_arquivo):
      """Ler no arquivo texto as urls cadastradas""" 
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
          print()
          print('Página não encontrada!')
          self.__teste=False
        
        return self.__teste
    
          
  