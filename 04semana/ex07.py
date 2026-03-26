from math import sqrt

a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))

delta = b ** 2 - (4 * a * c)

if delta < 0:
    print("A equação não possui raízes reais.")

elif delta == 0:
    x = -b / (2 * a)
    print("A equação possui uma raiz real (raiz dupla):")
    print("x = %.2f" % x)

else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print("A equação possui duas raízes reais:")
    print("x1 = %.2f" % x1)
    print("x2 = %.2f" % x2)
