'''
l = []
while True:
    n = int(input('Digite um número (0 sai): '))
    if n == 0:
        break
    l.append(n)
maximo = l[0]
for i in l:
    if i > maximo:
        maximo = i
print(maximo)
'''

l = [47, 55, 1, 7, 2, 4, 45]

maximo = l[0]
for e in l:
    if e < maximo:
        maximo = e
print(f'{maximo} é o maximo')


