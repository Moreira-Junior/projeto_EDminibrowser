# Importando funções dos outros módulos
from paginas import Pagina
# from historico import Historico
# from texto import Adicionador
from navegador import Navegador

#criação do objeto historico1 que será a pilha sequencial
n1=Navegador('sites.txt')

#loop para inserção do usuário das páginas desejadas
while True:
    print()
    try:
        print(f'Páginas visitadas: {n1.mostra_historico()}')
    except:
        print(f'Páginas visitadas: ')
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
            n1.empilhar(url)
    except:
        pass
    


    #funcionalidade back, retornando a página anterior na pilha  
    if ent=='#back':
        if n1.pilha_vazia():
            print('Não há página no histórico ainda!')
        else:
            n1.voltar()
            url=n1.topo_pilha()
            if n1.tamanho()>=1:
                n1.voltar()
            else:
                n1.__init__('sites.txt')
                del url
    
    #funcionalidade add, adicionando uma nova url e escrevendo-a no banco de urls em txt
    elif ent.split(' ')[0]=='#add':    
        print('Digite a nova url: ')
        teste=ent.split(' ')[1]
        # teste='\n'+teste
        # n1.adicionar(teste)
        # novaurl=Adicionador(teste)
        
        if n1.forma(teste):
            n1.adicionar(teste)
            print('Página Adicionada!')
            try:
                if n1.topo_pilha()==url:
                    n1.voltar()
            except:
                pass
        else:
            print('Página Inválida!')
            try:
                if n1.topo_pilha()==url:
                    n1.voltar()
            except:
                pass
        # if novaurl.forma():
        #     novaurl.add('sites.txt')
        #     try:
        #         if h1.topo()==url:
        #             h1.remover()
        #     except:
        #         pass
        # else:
        #     try:
        #         if h1.topo()==url:
        #             h1.remover()
        #     except:
        #         pass
        #     print('Formato de página inválido!')
    
    #funcionalidade para imprimir o histórico de páginas visitadas
    elif ent=='#showhist':
        print(n1.mostra_historico())
        try:
            if n1.topo_pilha()==url:
                n1.voltar()
        except:
            pass
        input('Pressione ENTER para continuar')

    #funcionalidade para informar quais comandos poderão ser utilizados pelo usuário
    elif ent=='#help':
        print('''================Help do navegador================
        comando:                função:
        #sair                   finaliza o navegador
        #add                    adiciona uma página
        #back                   voltar para página anterior
        #showhist               mostrar o histórico de navegação
        ''')
        try:
            if n1.topo_pilha()==url:
                n1.voltar()
        except:
            pass
        input('Pressione ENTER para continuar')
    
    #comando que encerra o loop e finaliza o programa
    elif ent=='#sair':
        print('Fim do programa!')
        break

        #condição para digitação da url, com resultados possíveis de página válida ou inválida
    # if ent!='#sair' and ent!='#back' and ent!='#help' and ent!='#add' and ent!='#showhist' and ent!='#help':
      #loop de inserção de página, verificando se ela existe no banco de dados em txt
    else:
      while True:
        url=Pagina(ent)
        if n1.existencia(url):
          break
        else:
          print('Digite novamente a página: ')
          ent=input()
          ent=ent.lower()
          if ent=='#sair' or ent=='#back' or ent=='#help' or ent=='#add' or ent=='#showhist' or ent=='#help':
            del url
            break