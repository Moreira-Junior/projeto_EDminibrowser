from navegador import Navegador

#criação do objeto navegador 1 que controlará as outras classes
navegador1=Navegador('sites.txt')
#loop para inserção do usuário das páginas desejadas
while True:
    print()
    try:
        print(f'Páginas visitadas: {navegador1.mostra_historico()}')
    except:
        print(f'Páginas visitadas: ')
    try:
        print(f'Home: {url}')
    except:
        print(f'Home: ') 
    print()
    print('Páginas internas: ')
    try:
        if navegador1.pegar_filho_esq(url) is None:
            print('')
        else:
            print(navegador1.pegar_filho_esq(url))
        # url.resetCursor()
        if navegador1.pegar_filho_dir(url) is None:
            print('')
        else:
            print(navegador1.pegar_filho_dir(url))
    except:
        print('')
    print()
    print('Renderizador:')
    try:
        render=url.replace('/','.',4)
        print(navegador1.renderizar(render))
        print()
    except:
        print('')

    print('Digite a url ou #back para retornar à última página visitada.')
    print('Para entrar numa página interna, digite /"paginaInterna"!')
    print('Para abrir a ajuda, digite #help!')
    ent=input()
    ent=ent.lower()

    try:
        if str(url)==ent:
            print('Você já está nessa página!')
        else:
            navegador1.empilhar(url)
    except:
        pass
    

    #funcionalidade back, retornando a página anterior na pilha  
    if ent=='#back':
        if navegador1.pilha_vazia():
            print('Não há página no histórico ainda!')
        else:
            navegador1.voltar()
            url=navegador1.topo_pilha()
            if navegador1.tamanho()>=1:
                navegador1.voltar()
            else:
                navegador1.__init__('sites.txt')
                del url

    #funcionalidade para informar quais comandos poderão ser utilizados pelo usuário
    elif ent=='#help' or ent=='':
        print('''================Help do navegador================
        comando:                função:
        #sair                   finaliza o navegador
        #add                    adiciona uma página
        #back                   voltar para página anterior
        #showhist               mostrar o histórico de navegação
        ''')
        try:
            if navegador1.topo_pilha()==url:
                navegador1.voltar()
        except:
            pass
        input('Pressione ENTER para continuar')

    #funcionalidade add, adicionando uma nova url e escrevendo-a no banco de urls em txt
    elif ent.split(' ')[0]=='#add':    
        try:
            teste=ent.split(' ')[1]
            if navegador1.forma(teste):
                navegador1.adicionar(teste)
                try:
                    if navegador1.topo_pilha()==url:
                        navegador1.voltar()
                except:
                    pass
            else:
                print('Página Inválida!')
                try:
                    if navegador1.topo_pilha()==url:
                        navegador1.voltar()
                except:
                    pass
        except:
            print('Digite a página na mesma linha do comando #add')
    
    #funcionalidade para imprimir o histórico de páginas visitadas
    elif ent=='#showhist':
        print(navegador1.mostra_historico())
        try:
            if navegador1.topo_pilha()==url:
                navegador1.voltar()
        except:
            pass
        input('Pressione ENTER para continuar')
    
    #comando que encerra o loop e finaliza o programa
    elif ent=='#sair':
        print('Fim do programa!')
        break

    elif ent=='':
        try:
            if navegador1.topo_pilha()==url:
                navegador1.voltar()
        except:
            pass
    #comando para acessar paginas internas    
    elif ent[0]=='/':
        teste_url = url +'/' +ent.strip('/')
        if navegador1.existencia(teste_url):
            url = url +'/' +ent.strip('/')
        else:
            print('Página Inválida')
            navegador1.voltar()
    
    #entrada de url
    else:
      while True:
        url=ent
        if navegador1.existencia(url):
          break
        else:
          print('Digite novamente a página: ')
          ent=input()
          ent=ent.lower()
          if ent=='#sair' or ent=='#back' or ent=='#help' or ent=='#add' or ent=='#showhist' or ent=='#help':
            del url
            break