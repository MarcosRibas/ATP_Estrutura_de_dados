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

print('********** \33[34mArvore Binária de Busca\33[m **********')
while True:
    print('Digite:\n[ \33[34m1\33[m ] Para inserir um dado em um arquivo\n[ \33[34m2\33[m ] Para buscar um termo\n[ \33[34m3\33[m ] Para mostrar todos os dados cadastrados\n[ \33[34m4\33[m ] Para sair  ')
    sleep(1)
    while True: 
        m = input("Qual a opção escolhida? ")
        if m.isnumeric():
            menu = int(m)
            break
        else:
            print('\33[31mERRO! Digite um número inteiro de 1 à 4\33[m')
    if menu == 1:
        while True:
            print('Digite:\n[ \33[34m1\33[m ] Para inserir um dado no arquivo1\n[ \33[34m2\33[m ] Para inserir um dado no arquivo2\n[ \33[34m3\33[m ] Para inserir um dado no arquivo3\n[ \33[34m4\33[m ] Para inserir um dado no arquivo4\n[ \33[34m5\33[m ] Para inserir um dado no arquivo5\n[ \33[34m6\33[m ] Para retornar ao menu inicial')
            sleep(1)
            while True:
                o = input("Qual a opção escolhida? ")
                if o.isnumeric():
                    opçao = int(o)
                    break
                else:
                    print('\33[31mErro! Digite um número inteiro de 1 à 6.\33[m')
            if opçao == 1:
                termo = input("Qual palavra você quer inserir? \n").strip().lower()
                arvore.inserirArv(termo, arquivo1)
                sleep(1)                
                print(f'\33[32mPalavra "{termo}" inserida com sucesso!\33[m')
                print('*' * 45) 
                sleep(1)
            elif opçao == 2:
                termo = input("Qual palavra você quer inserir? \n").strip().lower()
                arvore.inserirArv(termo, arquivo2)
                sleep(1)
                print(f'\33[32mPalavra "{termo}" inserida com sucesso!\33[m')
                print('*' * 45)
                sleep(1)
            elif opçao == 3:
                termo = input("Qual palavra você quer inserir? \n").strip().lower()
                arvore.inserirArv(termo, arquivo3)
                sleep(1)
                print(f'\33[32mPalavra "{termo}" inserida com sucesso!\33[m')
                print('*' * 45)
                sleep(1)
            elif opçao == 4:
                termo = input("Qual palavra você quer inserir? \n").strip().lower()
                arvore.inserirArv(termo, arquivo4)
                sleep(1)
                print(f'\33[32mPalavra "{termo}" inserida com sucesso!\33[m')
                print('*' * 45)
                sleep(1)
            elif opçao == 5:
                termo = input("Qual palavra você quer inserir? \n").strip().lower()  
                arvore.inserirArv(termo, arquivo5)
                sleep(1)
                print(f'\33[32mPalavra "{termo}" inserida com sucesso!\33[m')
                print('*' * 45)
                sleep(1)
            elif opçao == 6:
                print('*' * 45)
                break           
            else:
                print('\33[31mDiscagem incorreta, tente novamente\33[m')
    elif menu == 2:
        dado = str(input('Qual dado deseja pesquisar? Caso desejar pesquisar mais de um dado, separe-os por espaços\n')).split()
        print('*' * 45)
        cont = 0
        for c in dado:
            d2 = {'Arquivo1': arquivo1.buscaLista(c.lower().strip()),'Arquivo2': arquivo2.buscaLista(c.lower().strip()),'Arquivo3': arquivo3.buscaLista(c.lower().strip()),'Arquivo4': arquivo4.buscaLista(c.lower().strip()),'Arquivo5': arquivo5.buscaLista(c.lower().strip())}
            text = ''
            for a, f in sorted(d2.items(), key=itemgetter(1), reverse=True):
                text += f'O \33[34m{a}\33[m tem {f} vez(es) a palavra \33[32m{dado[cont].lower()}\33[m\n'
            cont += 1
            print(text)
            print('*' * 45)
            d2 = {} 
        sleep(1)
    elif menu == 3:
        print('**** \33[34mArvore de arquivos:\33[m ****')
        arvore.buscarArv()        
        print()
        print('\33[34mArquivo1:\33[m')
        print(arquivo1)
        print('\33[34mArquivo2:\33[m')
        print(arquivo2)
        print('\33[34mArquivo3:\33[m')
        print(arquivo3)
        print('\33[34mArquivo4:\33[m')
        print(arquivo4)
        print('\33[34mArquivo5:\33[m')
        print(arquivo5)
    elif menu == 4:
        print('Saindo...')
        break
    else:
        print('\33[31mDiscagem incorreta, tente novamente\33[m')
        sleep(1)

   



















