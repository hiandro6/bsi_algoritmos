print("===== COMO SÃO SEUS HÁBITOS DE ESTUDOS =====")

print("""
1. Você costuma estudar com horário definido?
a) Sempre (+2 pontos)
b) Às vezes (+1 ponto)
c) Nunca (0 pontos)
""")
p1 = int(input("pontuação: "))


print("""
2. Quando recebe uma atividade, você:
a) Começa logo (+2 pontos)
b) Deixa para depois, mas faz (+1 ponto)
c) Só lembra no último momento (0 pontos)
""")
p2 = int(input("pontuação: "))

print("""
3. Você anota prazos e compromissos?
a) Sim, sempre (+2 pontos)
b) Às vezes (+1 ponto)
c) Não (0 pontos)
""")
p3 = int(input("pontuação: "))

print("""
4. Durante os estudos, você se distrai com facilidade?
a) Raramente (+2 pontos)
b) Às vezes (+1 ponto)
c) Frequentemente (0 pontos)
""")
p4 = int(input("pontuação: "))

p_total = p1 + p2 + p3 + p4
print(f" sua pontuação final foi {p_total}")
print ("""
Classificação final:
7 a 8 pontos → Perfil muito organizado
4 a 6 pontos → Perfil moderadamente organizado
0 a 3 pontos → Perfil pouco organizado
""")
