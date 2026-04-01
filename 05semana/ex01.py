dia = int(input("informe o dia de hoje[n°]: "))
mes = int(input("informe o mês atual[n°]: "))
hemisferio = input("informe o seu hemisfério[norte ou sul]: ")

if hemisferio.lower() == "sul":
    if (mes == 9 and dia >= 22) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        estacao = "primavera"
    elif (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 21):
        estacao = "verão"
    elif (mes == 3 and dia >= 22) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 21):
        estacao = "outono"
    elif (mes == 6 and dia >= 22) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 21):
        estacao = "verão"
    
elif hemisferio.lower() == "norte":
    pass
else:
    print("digite um hemisfério válido")
