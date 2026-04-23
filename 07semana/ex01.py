import random

jogar_novamente = ""

while jogar_novamente != "N":
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    if soma == 7 or soma == 11:
        print("a soma dos dados foi %d, parabéns você ganhou!"%(soma))
    else:
        print("a soma dos dados foi %d, não foi dessa vez"%(soma))
    jogar_novamente = input("gostaria de jogar novamente? (S/N): ").upper()
