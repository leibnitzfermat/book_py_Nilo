
# a = set([1,2,3,4])
a = {2,5,8,4,8}
b = {7,8,2,1,5}

print(f'Primeira lista {a}')
print(f'Primeira lista {b}')

print(f'Os valores comuns entre as lista são: {a & b}')  #{a.intersection(b)}

print(f'Os valores existente apenas na primeira lista: {a-b}')
# uso do metodo a.difference(b) e valido
print(f'Os valores existente apenas na segunda lista: {b-a}')

print(f'lista com valores não repetidos de ambas as listas: {a ^ b}')
#a ^ b = a - b | b - a

#print(f'lista com valores não repetidos de ambas as listas: {(a ^ b == a - b | b - a)}') #True
