import math

a = float (input("Coeficiente A: "))
b = float (input("Coeficiente B: "))
c = float (input("Coeficiente C: "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("A equação não possui raizes reais")
elif delta == 0:
    print(f"A equação possui raizes reais.")
else: 
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"As raizes reais são: x1 = {x1} e x2 = {x2}")