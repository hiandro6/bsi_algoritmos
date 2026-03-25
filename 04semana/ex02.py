nome1 = input("digite o nome do 1° usuário: ")
idade1 = int(input("digite a idade do 1° usuário: "))

nome2 = input("digite o nome do 2° usuário: ")
idade2 = int(input("digite a idade do 2° usuário: ")) 

if idade1 > idade2:
    print(f"{nome1} é mais velho que {nome2}")

elif idade2 > idade1:
    print(f"{nome2} é mais velho que {nome1}")

else:
    print(f"{nome1} e {nome2} têm a mesma idade")
