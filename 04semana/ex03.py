nome1 = input("digite o nome do 1° usuário: ")
idade1 = int(input("digite a idade do 1° usuário: "))

nome2 = input("digite o nome do 2° usuário: ")
idade2 = int(input("digite a idade do 2° usuário: ")) 

diferenca = idade1 - idade2
if diferenca < 0:
    diferenca = diferenca * (-1)

print(f"a diferença de idade entre eles é {diferenca}")
