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
    
lista3 = lista1[:]

x = 0

while True:
    if lista3[x] in lista2:
        break
    else:
        lista3.append(lista2[x])
        print(lista3)
    x += 1

print(lista3)  