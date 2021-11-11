from paginas import Pagina
from historico import Historico

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
        h1.inserir(url)
    except:
        pass

    if ent!='#sair' and ent!='#back' and ent!='#help':
        url=Pagina(ent)
      
    if ent=='#back':
        h1.remover()
        url=h1.topo()
        if h1.tamanho()>=1:
            h1.remover()
        else:
            h1.__init__()
            del url
        
    if ent=='#sair':
        print('Fim do programa!')
        break