from random import randint
from os import system
from time import sleep


def clear():
	system('cls')


def lerint(msg):
	while True:
		try:
			inteiro = int(input(msg))
		except:
			pass
		else:
			return inteiro


def main():
	while True:
		clear()
		computador = randint(1, 20)
		op = lerint("Suas opções\n[ 1 ]NOVO JOGO\n[ 2 ]ESTATÍSTICAS\n[ 3 ]SAIR\nSua escolha: ")

		match op:
			case 1:
				tentativas = 0
				print("PENSEI EM UM NÚMERO ENTRE 1 E 20, TENTE ADIVINHAR!")
				while True:
					jogador = int(input("Seu palpite: "))
					tentativas += 1
					if jogador == computador:
						print("Jogador VENCEU!")
						sleep(3)
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
					voltar = lerint("\nDigite 0 para voltar: ")
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


if __name__ == '__main__':
	main()