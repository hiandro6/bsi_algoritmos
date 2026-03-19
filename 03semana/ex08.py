from math import log, ceil
print('Matemática Financeira')
print('Tempo necessário para obtenção de valor')
capital = float(input('Quanto você deseja investir? R$ '))
montante = float(input('Quanto você quer retirar? R$ '))
taxa_juros = float(input('Qual a taxa de juros mensal? (%): ')) / 100

#M = C(1 + i)**t
#(M / C) = (1 + i)**t
#log (M / C) = log (1 + i)**t
#log (M / C) = t . log (1 + i)
#t = log (M / C) / log (1 + i)

tempo = log(montante / capital) / log(1 + taxa_juros)
tempo = ceil(tempo)
print(f"você precisará de {tempo} meses para atingir o montante desejado")
