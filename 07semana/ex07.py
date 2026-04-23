import random

contador = 0
numero = random.randint(1, 9)
while contador < 3:
    tentativa = int(input("advinhe o número (1 a 9):"))
    contador += 1
    if tentativa == numero:
        if contador == 1:
            print("você teve muita sorte!")
        contador = 3
        print("você acertou!")
    elif tentativa < numero:
        print("digite um número maior")
    elif tentativa > numero:
        print("digite um número menor")
