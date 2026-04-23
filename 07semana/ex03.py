import random

jogar_novamente = ""

while jogar_novamente != "N":
    jogador1 = random.choice(["PEDRA", "PAPEL", "TESOURA"])
    jogador2 = input("PEDRA, PAPEL ou TESOURA? ").upper()
    print("jogador 1: %s, jogador 2(você): %s, "%(jogador1, jogador2))

    if jogador1 == "PEDRA" and jogador2 == "TESOURA":
        print("jogador 1 ganhou")
    elif jogador1 == "PAPEL" and jogador2 == "PEDRA":
        print("jogador 1 ganhou")
    elif jogador1 == "TESOURA" and jogador2 == "PAPEL":
        print("jogador 1 ganhou")
    elif jogador2 == "PEDRA" and jogador1 == "TESOURA":
        print("jogador 2(você) ganhou")
    elif jogador2 == "PAPEL" and jogador1 == "PEDRA":
        print("jogador 2(você) ganhou")
    elif jogador2 == "TESOURA" and jogador1 == "PAPEL":
        print("jogador 2(você) ganhou")
    else:
        print("empate, ninguém ganhou")
    jogar_novamente = input("gostaria de jogar novamente? (S/N): ").upper()
