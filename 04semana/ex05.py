from datetime import date
data_nasc = input("digite sua data de nascimento: [ dd/mm/yyyy ]: ")

data_nasc = data_nasc.split("/")
ano_nasc = int(data_nasc[2])
mes_nasc = int(data_nasc[1])
dia_nasc = int(data_nasc[0])

ano_atual = date.today().year
mes_atual = date.today().month
dia_atual = date.today().day

idade = ano_atual - ano_nasc
if mes_atual < mes_nasc:
    idade = idade - 1
elif mes_atual == mes_nasc:
    if dia_nasc > dia_atual:
        idade = idade - 1
print(f"sua idade é {idade}")
