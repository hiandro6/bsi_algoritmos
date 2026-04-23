import random

contador = 0
numero = random.randint(1, 100)
while contador < 10:
    tentativa = int(input("advinhe o número (1 a 100):"))
    contador += 1
    if tentativa < 1 or tentativa > 100:
        print("palpite inválido, você foi desclassificado!")
        contador = 10
    elif tentativa == numero:
        if contador < 3:
            print("você teve muita sorte!")
        elif contador < 6:
            print("você joga bem, mas ainda contou com a sorte")
        elif contador <= 10:
            print("você é um excelente estrategista")
        print("foram necessárias %d tentativas para você acertar" % (contador))
        contador = 10
    elif tentativa != numero:
        if tentativa < numero:
            print("digite um número maior")
        elif tentativa > numero:
            print("digite um número menor")
        if contador == 10:
            print("analise sua estratégia melhor antes")
