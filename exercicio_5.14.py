s = 0
contador = 0
while True:
	v = int(input("Digite um número a somar ou 0 para sair: "))
	if v == 0:
		break
	contador += 1
	s += v
print(f'A quantidade de numero digitados foi:{contador}, a soma total foi:{s}, e a média: {s / contador:.2f}')

'''
soma = 0
quantidade = 0
while True:
	n = int(input("Digite um número inteiro:"))
    if n==0:
        break;
    soma = soma + n
    quantidade = quantidade + 1
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print("Média: %10.2f" % (soma/quantidade))
'''