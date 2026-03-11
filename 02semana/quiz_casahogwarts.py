print("""
 QUAL SERIA SUA CASA EM HOGWARTS?

Responda às perguntas e anote a pontuação correspondente à alternativa escolhida.

1. Qual qualidade você mais valoriza?

a) Coragem (+2 pontos)
b) Inteligência (+1 ponto)
c) Ambição (+0 pontos)
""")

p1 = int(input("informe sua pontuação: "))

print("""
2. Se você encontra um desafio difícil em Hogwarts, você:

a) Enfrenta sem medo (+2 pontos)
b) Analisa a situação antes de agir (+1 ponto)
c) Procura uma forma de se beneficiar da situação (+0 pontos)
""")
p2 = int(input("informe sua pontuação: "))


print("""
3. Qual dessas atividades você preferiria?

a) Participar de uma aventura perigosa (+2 pontos)
b) Estudar novos feitiços na biblioteca (+1 ponto)
c) Planejar estratégias para vencer os outros alunos (+0 pontos)
""")
p3 = int(input("informe sua pontuação: "))



print("""
4. Se um amigo precisa de ajuda, você:

a) Ajuda imediatamente (+2 pontos)
b) Ajuda se souber como resolver (+1 ponto)
c) Avalia se vale a pena ajudar (+0 pontos)
""")
p4 = int(input("informe sua pontuação: "))

p_total = p1 + p2 + p3 + p4

print(f"sua pontuação é {p_total}")
print("""
Resultado:

7 a 8 pontos → Casa Gryffindor
Você é corajoso, determinado e gosta de enfrentar desafios, como Harry Potter.

4 a 6 pontos → Casa Ravenclaw
Você valoriza inteligência, criatividade e conhecimento.

2 a 3 pontos → Casa Hufflepuff
Você é leal, dedicado e valoriza a amizade.

0 a 1 ponto → Casa Slytherin
Você é ambicioso, estratégico e determinado a alcançar seus objetivos.
""")
