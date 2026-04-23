import random
jogar_novamente = ""
while jogar_novamente != "N":
    contador = 0
    numero = random.randint(1, 9)
    while contador < 3:
        tentativa = int(input("advinhe o número (1 a 9):"))
        contador += 1
        if tentativa == numero:
            if contador == 1:
                print("você teve muita sorte!")
            elif contador == 2:
                print("você joga bem, mas ainda contou com a sorte")
            elif contador == 3:
                print("você é um excelente estrategista")
            contador = 3
        if tentativa != numero:
            if tentativa < numero:
                print("digite um número maior")
            elif tentativa > numero:
                print("digite um número menor")
            if contador == 3:
                print("analise sua estratégia melhor antes")
    jogar_novamente = input("quer jogar novamente?(S/N):").upper()
