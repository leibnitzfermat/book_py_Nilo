n = float(input("Digite um mumero para aproximação: "))
b = 2

while abs(n - b**2) > 0.0001:
    p = (b+(n/b))/2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:8.10f}")    