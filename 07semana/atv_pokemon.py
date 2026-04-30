votos = {
    "charmander": 0,
    "bulbasaur": 0,
    "squirtle": 0,
    "nenhum": 0
}

invalido = 0
pessoa = 0

resp = input("Você deseja responder à pesquisa (s/n)? ").upper()

while resp != "N":
    pessoa += 1
    print("\nEntrevistando a %d° pessoa." % pessoa)

    voto = input("Escolha C - charmander, B - bulbasaur, S - squirtle ou NENHUM: ").upper()

    if voto == "C":
        print("Você optou pelo pokemon charmander!")
        votos["charmander"] += 1

    elif voto == "B":
        print("Você optou pelo pokemon bulbasaur!")
        votos["bulbasaur"] += 1

    elif voto == "S":
        print("Você optou pelo pokemon squirtle!")
        votos["squirtle"] += 1

    elif voto == "NENHUM":
        print("Ok, você não gosta desses pokemons")
        votos["nenhum"] += 1

    else:
        print("opção inválida, vote novamente!")
        invalido += 1
        pessoa -= 1

    resp = input("Você deseja responder à pesquisa (s/n)? ").upper()


total = pessoa + invalido

print("\nRESULTADOS:")
print("%d pessoas foram entrevistadas." % pessoa)

# ordenar pelo número de votos
ordenado = sorted(votos.items(), key=lambda x: x[1], reverse=True)

for nome, qtd in ordenado:
    if pessoa > 0:
        p_valido = qtd / pessoa * 100
    else:
        p_valido = 0

    if total > 0:
        p_total = qtd / total * 100
    else:
        p_total = 0

    print("total de votos para %s : %d | percentual válido: %.2f%% | percentual total: %.2f%%"
          % (nome, qtd, p_valido, p_total))

print("Votos inválidos:", invalido)
