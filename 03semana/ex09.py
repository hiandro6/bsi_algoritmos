from math import log

print("Crescimento Populacional")
print("Tempo para obtenção de uma população")

pop_atual = int(input("Qual a população atual? "))
tx_cresc = float(input("Taxa de crescimento estimada? "))
tx_cresc = 1 + (tx_cresc / 100)
pop_esper = float(input("Qual a população esperada? "))

fator_cresc = pop_esper / pop_atual
tempo = log(fator_cresc) / log(tx_cresc)

print(f" serão {tempo:.1f} anos para obter essa população")
