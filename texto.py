

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
  
      
