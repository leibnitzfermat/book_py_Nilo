lista1 = []
lista2 = []

while True:
    l1 = int(input("Digite um valor para 1ª lista (0 para sair): "))
    if l1 == 0:
        break
    lista1.append(l1)
while True:
    l2 = int(input("Digite um valor para 2ª lista (0 para sair): "))
    if l2 == 0:
        break
    lista2.append(l2)
    
lista3 = lista1[:] + lista2[:]
print(f'3ª lista {lista3}')
x = 0
while x < len(lista3):
    print(f'{x + 1}º elemento: {lista3[x]}')  # incremento de X + 1 para leitura humana simples
    x += 1