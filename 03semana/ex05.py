# calculando a área de um conjunto de terrenos
largura1 = float(input("informe a largura do 1° ambiente: "))
comprimento1 = float(input("informe o comprimento do 1°ambiente: "))

area1 = largura1 * comprimento1

largura2 = float(input("informe a largura do 2° ambiente: "))
comprimento2 = float(input("informe o comprimento do 2°ambiente: "))

area2 = largura2 * comprimento2

largura3 = float(input("informe a largura do 3° ambiente: "))
comprimento3 = float(input("informe o comprimento do 3°ambiente: "))

area3 = largura3 * comprimento3

area_total = area1 + (2 * area2) + (2 * area3)
print(f"a área do terreno é de {area_total:.2f} m²")
