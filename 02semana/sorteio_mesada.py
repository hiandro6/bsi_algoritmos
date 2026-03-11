from random import randint
valores = [20, 40, 80, 100]
filhos = ["HUGUINHO", "ZEZINHO", "LUIZINHO"]
print("===================================")
print("======== SORTEIO DA MESADA ========")
print("===================================")
for i in filhos:
    valor = valores[randint(0, 3)]
    print(f"===   {i:10} : {valor:10}   ===")
print("===================================")
