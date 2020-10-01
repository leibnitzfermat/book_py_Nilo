l = [10,7,27,39]
p = int(input('Digite o valor a procurar: '))
achou = False
x = 0
while x < len(l):
    if l[x] == p:
        break
    x += 1
if x < len(l):
    print(f'{p} achado na posição {x}')
else:
    print(f'{p} não encontrado')