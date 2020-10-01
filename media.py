x = 1
soma = 0
diviso = 0
while x <= 5:
	n = int(input(f'{x} Digite o número: '))
	soma = soma + n
	x += 1
	diviso += 1
print(f"Média: {soma / diviso :5.2f}")
