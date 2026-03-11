print("==== DESCUBRA SEU PESO IDEAL ===")

sexo = input("digite seu sexo: [F/M]")
sexo = sexo.upper()
altura = int(input("digite sua altura em cm: "))

if sexo == "F":
    peso_ideal = (altura - 100) - ((altura - 150) / 2)
elif sexo == "M":
    peso_ideal = (altura - 100) - ((altura - 150) / 4)

print(f"seu peso ideal é {peso_ideal}")
