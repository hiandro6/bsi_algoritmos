import random

continuar = True
vitorias_j1 = 0
vitorias_j2 = 0
while continuar:
    jogador1 = random.choice(["PEDRA", "PAPEL", "TESOURA"])
    jogador2 = input("PEDRA, PAPEL ou TESOURA? ").upper()
    print("jogador 1: %s, jogador 2(você): %s, "%(jogador1, jogador2))

    if jogador1 == "PEDRA" and jogador2 == "TESOURA":
        print("jogador 1 ganhou")
        vitorias_j1 += 1
    elif jogador1 == "PAPEL" and jogador2 == "PEDRA":
        print("jogador 1 ganhou")
        vitorias_j1 += 1
    elif jogador1 == "TESOURA" and jogador2 == "PAPEL":
        print("jogador 1 ganhou")
        vitorias_j1 += 1
    elif jogador2 == "PEDRA" and jogador1 == "TESOURA":
        print("jogador 2(você) ganhou")
        vitorias_j2 += 1
    elif jogador2 == "PAPEL" and jogador1 == "PEDRA":
        print("jogador 2(você) ganhou")
        vitorias_j2 += 1
    elif jogador2 == "TESOURA" and jogador1 == "PAPEL":
        print("jogador 2(você) ganhou")
        vitorias_j2 += 1
    else:
        print("empate, ninguém ganhou")
    print("o jogador 1 ganhou %d vezes e o jogador 2(você) ganhou %d vezes" % (vitorias_j1, vitorias_j2))
    if vitorias_j1 == 5 or vitorias_j2 == 5:
        continuar = False
        
