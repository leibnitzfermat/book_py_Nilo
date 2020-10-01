notas = [6, 7, 5, 8, 9]

soma = 0
x = 0

while x < 5:
    soma += notas[x]
    x += 1
print(f'Média: {soma / len(notas):5.2f}')


'''
media = 0
for x in notas:
    media += x
print(f'{media / 5:.2f}')
'''