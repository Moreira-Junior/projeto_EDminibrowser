# Importando funções dos outros módulos
from paginas import Pagina
from historico import Historico
from texto import Adicionador

#criação do objeto historico1 que será a pilha sequencial
h1=Historico()

#loop para inserção do usuário das páginas desejadas
while True:
    print()
    print(f'Páginas visitadas: {h1}')
    try:
        print(f'Home: {url}')
    except:
        print(f'Home: ') 
    print('Digite a url ou #back para retornar à última página visitada.')
    print('Para abrir a ajuda, digite #help!')
    ent=input()
    ent=ent.lower()
    try:
        if str(url)==ent:
            print('Você já está nessa página!')
        else:
            h1.inserir(url)
    except:
        pass
    
    #condição para digitação da url, com resultados possíveis de página válida ou inválida
    if ent!='#sair' and ent!='#back' and ent!='#help' and ent!='#add' and ent!='#showhist' and ent!='#help':
      #loop de inserção de página, verificando se ela existe no banco de dados em txt
      while True:
        url=Pagina(ent)
        if url.ler_arquivo('sites.txt'):
          break
        else:
          print('Digite novamente a página: ')
          ent=input()
          ent=ent.lower()
          if ent=='#sair' or ent=='#back' or ent=='#help' or ent=='#add' or ent=='#showhist' or ent=='#help':
            del url
            break

    #funcionalidade back, retornando a página anterior na pilha  
    if ent=='#back':
        if h1.vazio():
            print('Não há página no histórico ainda!')
        else:
            h1.remover()
            url=h1.topo()
            if h1.tamanho()>=1:
                h1.remover()
            else:
                h1.__init__()
                del url
    
    #funcionalidade add, adicionando uma nova url e escrevendo-a no banco de urls em txt
    if ent=='#add':    
        print('Digite a nova url: ')
        teste=input()
        teste='\n'+teste
        novaurl=Adicionador(teste)
        if novaurl.forma():
            novaurl.add('sites.txt')
            try:
                if h1.topo()==url:
                    h1.remover()
            except:
                pass
        else:
            try:
                if h1.topo()==url:
                    h1.remover()
            except:
                pass
            print('Formato de página inválido!')
    
    #funcionalidade para imprimir o histórico de páginas visitadas
    if ent=='#showhist':
        h1.imprimir()
        try:
            if h1.topo()==url:
                h1.remover()
        except:
            pass
        input('Pressione ENTER para continuar')

    #funcionalidade para informar quais comandos poderão ser utilizados pelo usuário
    if ent=='#help':
        print('''================Help do navegador================
        comando:                função:
        #sair                   finaliza o navegador
        #add                    adiciona uma página
        #back                   voltar para página anterior
        #showhist               mostrar o histórico de navegação
        ''')
        try:
            if h1.topo()==url:
                h1.remover()
        except:
            pass
        input('Pressione ENTER para continuar')
    
    #comando que encerra o loop e finaliza o programa
    if ent=='#sair':
        print('Fim do programa!')
        break