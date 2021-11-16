

class Adicionador:
  """Classe para adiconar url no arquivo texto"""
  def __init__(self,novaurl):
    """Construtor para adicionar nova url"""
    self.__novaurl=novaurl
  

  def add(self,nome_arquivo):
    """Adiciona página nova no arquivo texto"""
    self.__existe=False
    with open(nome_arquivo) as arquivo:
      for i in arquivo:
        i=i.strip('\n')
        if i==self.__novaurl.strip('\n'):
          self.__existe=True
          print('Página já existe no banco de dados!')
      if not self.__existe:
        with open(nome_arquivo,'a') as arquivo:
          arquivo.write(self.__novaurl)
          print('Página adicionada') 
    
  def forma(self):
      self.__forma = self.__novaurl.split('.')
      self.__testf=True
      if self.__forma[0]=='\nwww':
          if self.__forma[-1]=='com' or self.__forma[-1]=='br' or self.__forma[-1]=='net':
              self.__testf=True
          else:
              self.__testf=False
      else:
          self.__testf=False
      return self.__testf  
