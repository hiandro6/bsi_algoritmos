#quantidade de arame para cercar uma fazenda
largura = float(input("informe o comprimento da fazenda: "))
comprimento = float(input("informe a largura da fazenda: "))
perimetro = (largura * 2) + (comprimento * 2)
quantidade_arame = perimetro * 5
print(f"você irá precisar de {quantidade_arame:.2f}m de arame para cercar sua fazenda")
