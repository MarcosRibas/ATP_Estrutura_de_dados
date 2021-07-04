from lista import ListaEncadeada
from arvore import Arvore
from time import sleep
from operator import itemgetter

arvore = Arvore()
arquivo1 = ListaEncadeada()
arquivo2 = ListaEncadeada()
arquivo3 = ListaEncadeada()
arquivo4 = ListaEncadeada()
arquivo5 = ListaEncadeada()
arquivo1.inserirLista('bola')
arquivo2.inserirLista('bola')
arquivo3.inserirLista('bola')
arquivo3.inserirLista('bola')
dado = str(input('Qual dado deseja pesquisar? Caso desejar pesquisar mais de um dado, separe-os por espaços\n')).split()

cont = 0
for c in dado:
    d2 = {}
    d2.clear()
    d2 = {'Arquivo1': arquivo1.buscaLista(c),'Arquivo2': arquivo2.buscaLista(c), 'Arquivo3': arquivo3.buscaLista(c), 'Arquivo4': arquivo4.buscaLista(c), 'Arquivo5':arquivo5.buscaLista(c)}
    for a, f in sorted(d2.items(), key=itemgetter(1), reverse=True):
        print(f'O {a} tem {f} vez(es) a palavra {dado[cont]}')              
    cont += 1
    print('*' * 25)
    d2 = {}
    d2.clear()
   

'''print('********** Arvore Binária de Busca **********')
while True:
    print('Digite:\n[ 1 ] Para inserir um dado em um arquivo\n[ 2 ] Para buscar um termo\n[ 3 ] Para mostrar todos os dados cadastrados\n[ 4 ] Para sair  ')
    sleep(1)
    menu = int(input("Qual a opção escolhida? "))
    if menu == 1:
        while True:
            print('Digite:\n[ 1 ] Para inserir um dado no arquivo1\n[ 2 ] Para inserir um dado no arquivo2\n[ 3 ] Para inserir um dado no arquivo3\n[ 4 ] Para inserir um dado no arquivo4\n[ 5 ] Para inserir um dado no arquivo5\n[ 6 ] Para retornar ao menu inicial')
            opçao = int(input("Qual a opção escolhida? "))            
            if opçao == 1:
                termo = input("Qual palavra você quer inserir? \n")
                arvore.inserirArv(termo, arquivo1)
                sleep(1)                
                print(f'Palavra "{termo}" inserida com sucesso!')
                print('*' * 45) 
                sleep(1)
            elif opçao == 2:
                termo = input("Qual palavra você quer inserir? \n")
                arvore.inserirArv(termo, arquivo2)
                sleep(1)
                print(f'Palavra "{termo}" inserida com sucesso!')
                print('*' * 45)
                sleep(1)
            elif opçao == 3:
                termo = input("Qual palavra você quer inserir? \n")
                arvore.inserirArv(termo, arquivo3)
                sleep(1)
                print(f'Palavra "{termo}" inserida com sucesso!')
                print('*' * 45)
                sleep(1)
            elif opçao == 4:
                termo = input("Qual palavra você quer inserir? \n")
                arvore.inserirArv(termo, arquivo4)
                sleep(1)
                print(f'Palavra "{termo}" inserida com sucesso!')
                print('*' * 45)
                sleep(1)
            elif opçao == 5:
                termo = input("Qual palavra você quer inserir? \n")  
                arvore.inserirArv(termo, arquivo5)
                sleep(1)
                print(f'Palavra "{termo}" inserida com sucesso!')
                print('*' * 45)
                sleep(1)
            elif opçao == 6:
                print('*' * 45)
                break           
            else:
                print('Discagem incorreta, tente novamente')
    elif menu == 2:
        dado = str(input('Qual dado deseja pesquisar? '))
        d2 = {'Arquivo1': arquivo1.buscaLista(dado),'Arquivo2': arquivo2.buscaLista(dado), 'Arquivo3': arquivo3.buscaLista(dado), 'Arquivo4': arquivo4.buscaLista(dado), 'Arquivo5':arquivo5.buscaLista(dado)}
        print(d2)
        for a, f in sorted(d2.items(), key=itemgetter(1), reverse=True):
            print(f'O {a} tem {f} vez(es) a palavra {dado}')
        print('*' * 40) 
        sleep(1)
    elif menu == 3:
        print('Arvore de arquivos:')
        arvore.imprimirArv()        
        print()
        print('Arquivo1:')
        print(arquivo1)
        print('Arquivo2:')
        print(arquivo2)
        print('Arquivo3:')
        print(arquivo3)
        print('Arquivo4:')
        print(arquivo4)
        print('Arquivo5:')
        print(arquivo5)
    elif menu == 4:
        print('Saindo...')
        break
    else:
        print('Discagem incorreta, tente novamente')'''

   



















