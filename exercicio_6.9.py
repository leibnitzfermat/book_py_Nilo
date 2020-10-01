
l = [10,7,27,39]
p = int(input('Digite o valor a procurar (p): '))
b = int(input('Digite o valor a procurar (b): '))
x = 0
achouP = False
achouB = False
primeiro = 0
while x < len(l):
    if l[x] == p:
        achouP = True
        if not achouB:
            primeiro = 1
    if l[x] == b:
        achouB = True
        if not achouP:
            primeiro = 2
    x += 1
if achouP:
    print(f'{p} achado')
else:
    print(f'{p} não encontrado')
if achouB:
    print(f'{b} achado')
else:
    print(f'{b} não encontrado')
if primeiro == 1:
    print('p achado primeiro que b')
elif primeiro == 2 :
    print('b achado primeiro que p')
