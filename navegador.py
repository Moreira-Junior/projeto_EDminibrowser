from paginas import Pagina
from historico import Historico
from texto import Adicionador

h1=Historico()


while True:
    print()
    print(f'Páginas visitadas: {h1}')
    try:
        print(f'Home: {url}')
    except:
        print(f'Home: ') 
    print('Digite a url ou #back para retornar à última página visitada.')
    ent=input()
    ent=ent.lower()
    try:
        # if url!=h1.topo():
        #     h1.inserir(url)
        h1.inserir(url)
    except:
        pass

    if ent!='#sair' and ent!='#back' and ent!='#help' and ent!='#add':

      while True:
        url=Pagina(ent)
        if url.ler_arquivo('sites.txt'):
          break
        else:
          print('Digite novamente a página: ')
          ent=input()
          ent=ent.lower()
          if ent=='#sair' or ent=='#back' or ent=='#help' or ent=='#add':
            del url
            break

      
    if ent=='#back':
      h1.remover()
      url=h1.topo()
      if h1.tamanho()>=1:
          h1.remover()
      else:
          h1.__init__()
          del url
    
    if ent=='#add':
      print('Digite a nova url: ')
      teste=input()
      teste='\n'+teste
      novaurl=Adicionador(teste)
      novaurl.add('sites.txt')
      if h1.topo()==url:
          h1.remover()
      
    if ent=='#sair':
        print('Fim do programa!')
        break