from random import randint
from os import system

def clear():
    system('cls')


while True:
    computador = randint(1, 20)
    op = int(input("\nSuas opções\n[ 1 ]NOVO JOGO\n[ 2 ]ESTATÍSTICAS\n[ 3 ]SAIR\nSua escolha: "))
    clear()
    match op:
        case 1:
            tentativas = 0
            print("PENSEI EM UM NÚMERO ENTRE 1 E 20, TENTE ADIVINHAR!")
            while True:
                jogador = int(input("Seu palpite: "))
                tentativas += 1
                if jogador == computador:
                    print("Jogador VENCEU!")
                    break
                elif computador > jogador:
                    print("O NÚMERO QUE EU PENSEI É MAIOR!\n")
                else:
                    print("O NÚMERO QUE EU PENSEI É MENOR!\n")
        case 2:
            while True:
                clear()
                print("ESTATÍSTICAS\n")
                print(f"Número de tentativas: {tentativas}")
                voltar = int(input("\nDigite 0 para voltar: "))
                if voltar == 0:
                    clear()
                    break
                else:
                    continue
                
        case 3:
            print("Obrigado, volte sempre!")
            break

        case _:
            continue