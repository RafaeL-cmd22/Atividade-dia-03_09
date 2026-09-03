catetoOposto = float(input("Digite o valor do cateto oposto:  "))
catetoAdjacente = float(input("Digite o valor do cateto adjacente:  "))

hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print(f"O valor da hipotenusa é: {hipotenusa}")
