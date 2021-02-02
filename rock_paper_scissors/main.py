import os
import random
import time


print("Bem Vindo(a) ao jogo Rock Paper Scissors!")
while True:
    print()
    print("------------------------------------------")
    print("Por favor selecione uma opção abaixo: ")
    print(" 1 - Rock (Pedra)")
    print(" 2 - Paper (Papel)")
    print(" 3 - Scissors (Tesoura)")
    print(" Q - Quit (Sair)")
    print("------------------------------------------")
    print()

    player_1 = input("Digite sua escolha em numeros: ")

    CHOICES = ["Pedra", "Papel", "Tesoura"]
    machine = random.choice(CHOICES)

    if player_1.upper() == "Q":
        break
    else:
        if player_1.isalpha():
            print(f"{player_1}, Não é uma opção válida")
        else:
            player_1 = int(player_1)
            if player_1 == 1 and machine == "Pedra":
                print(f"EMPATE!")
                print(f'Você escolheu "Pedra" e a CPU escolheu "{machine}".')
            elif player_1 == 1 and machine == "Papel":
                print("PERDEU!")
                print(f'Você escolheu "Pedra" e a CPU escolheu "{machine}".')
            elif player_1 == 1 and machine == "Tesoura":
                print("PARABÉNS VOCÊ GANHOU!")
                print(f'Você escolheu "Pedra" e a CPU escolheu "{machine}".')
            elif player_1 == 2 and machine == "Pedra":
                print("PARABÉNS VOCÊ GANHOU!")
                print(f'Você escolheu "Papel" e a CPU escolheu "{machine}".')
            elif player_1 == 2 and machine == "Papel":
                print("EMPATOU!")
                print(f'Você escolheu "Papel" e a CPU escolheu "{machine}".')
            elif player_1 == 2 and machine == "Tesoura":
                print("PERDEU!")
                print(f'Você escolheu "Papel" e a CPU escolheu "{machine}".')
            elif player_1 == 3 and machine == "Pedra":
                print("PERDEU!")
                print(f'Você escolheu "Tesoura" e a CPU escolheu "{machine}".')
            elif player_1 == 3 and machine == "Papel":
                print("PARABÉNS VOCÊ GANHOU!")
                print(f'Você escolheu "Tesoura" e a CPU escolheu "{machine}".')
            elif player_1 == 3 and machine == "Tesoura":
                print("EMPATE!")
                print(f'Você escolheu "Tesoura" e a CPU escolheu "{machine}".')
            else:
                print("Opção invalida")

            print("---------------------")
            SAIR = input('Para sair pressione "Q" ou pressione qualquer tecla para continuar. ')
            if SAIR.upper() == "Q":
                break
            print('-------------------')

        time.sleep(1)
