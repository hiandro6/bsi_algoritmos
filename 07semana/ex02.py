import random

jogar_novamente = ""

while jogar_novamente != "N":
    jogador1 = random.randint(0, 1)
    jogador2 = random.randint(0, 1)
    jogador3 = int(input("zerinho ou um? (0/1)"))
    print("jogador 1: %d, jogador 2: %d, jogador 3(você): %d, "%(jogador1, jogador2, jogador3))

    if jogador1 == 0 and jogador2 == 1 and jogador3 == 1:
        print("jogador 1 ganhou")
    elif jogador1 == 1 and jogador2 == 0 and jogador3 == 0:
        print("jogador 1 ganhou")
    elif jogador1 == 1 and jogador2 == 0 and jogador3 == 1:
        print("jogador 2 ganhou")
    elif jogador1 == 0 and jogador2 == 1 and jogador3 == 0:
        print("jogador 2 ganhou")
    elif jogador1 == 1 and jogador2 == 1 and jogador3 == 0:
        print("jogador 3 ganhou")
    elif jogador1 == 0 and jogador2 == 0 and jogador3 == 1:
        print("jogador 3 ganhou")
    else:
        print("empate, ninguém ganhou")
    jogar_novamente = input("gostaria de jogar novamente? (S/N): ").upper()
