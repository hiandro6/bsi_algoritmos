print("====CALCULE SEU IMC====")
peso = float(input("digite seu peso(kg): "))
altura = float(input("digite sua altura(m): "))
imc = peso / altura**2
print(f"seu imc é {imc}")
print("""
        TABELA IMC:

   IMC          Risco
  ≤ 18,5 - Abaixo do peso
    18,6 - 24,9 Saudável
    25,0 - 29,9 Sobrepeso
    30,0 - 34,9 Obesidade Grau I (leve)
    35,0 - 39,9 Obesidade Grau II (severa)
  ≥ 40,0 - Obesidade Grau III (mórbida)
""")
