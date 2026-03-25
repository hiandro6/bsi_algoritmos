import datetime
idade_limite = 60
print("Olá, prezado usuário!")
nome = input("Qual o seu nome? ")
ano_nasc = int(input("Em que ano você nasceu? "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc
print("%s, esse ano você completa %d anos"%(nome, idade))
if idade >= idade_limite:
    print("%s, você já se vacinou contra a COVID?"%nome)
    print("Estou vendo aqui que já chegou na sua faixa etária")
    print("Se não tomou ainda, procure um posto de saúde")
    print("Tenha um bom dia!")
