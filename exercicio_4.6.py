distancia = float(input("Qual a distancia que deseja percorrer: "))
if distancia <= 200:
    print(f"Preço: R${distancia * 0.50:.2f}")
else:
    print(f"Preço: R${distancia * 0.45:.2f}")
