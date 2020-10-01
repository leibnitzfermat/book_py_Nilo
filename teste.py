'''
produto1 = ["maça", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]
compras = [produto1, produto2, produto3]
for e in compras:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: {e[2]:.2f}")


compras = []
while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    compras.append([produto, quantidade, preco])
soma = 0.0
for e in compras:
    print(f"{e[0]:20s} x {e[1]:5d} {e[2]:5.2} {e[1] * e[2]:6.2f}")
    soma += e[1] * e[2]
print(f"Total: {soma:7.2}")

###############################################################################

consumo = int(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (R, C ou I): ")
if tipo == "R":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "I":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "C":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print("Erro ! Tipo de instalação desconhecido!")
custo = consumo * preco
print(f"Valor a pagar: R$ {custo:7.2f}")

################################################################

x = 1
while x <= 100:
    print(x)
    x += 1

    #ou

x = range(101)
for i in x:
    print(i)

#################################################################
from math import factorial
n = 5
print(factorial(n))

    #ou

n = int(input())
fatorial = 1

for x in range(1, n+1):
    print(x)
    fatorial = fatorial * x
print(fatorial)

    #ou

n = int(input("Digite: "))

step = n
fac = 1

while step > 0:
    print(step, end='x')
    fac = fac * step
    step -= 1
print(fac)

###################################################3

n = int(input("digite um numero: "))
ini = 1
while ini <= 10:
    print(f'{n} x {ini} = {n * ini}')
    ini += 1

# ou

n = int(input())

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")




def fatorial(n):
    print(f"Calculando o fatorial de {n}")
    if n == 0 or n == 1:
        return 1

    else:
        fat = n * fatorial(n - 1)
        print(f"fatorial de {n} = {fat}")
    return fat


fatorial(4)



n = int(input("digite: "))


for x in range(1, 11):
    print(f"{n} x {x} = {n * x}")

########################################

def reta(la, alt, cara ="*"):
    li = cara * la
    for i in range(alt):
        print(li)
        
reta(la = 3, alt = 4, cara="+")
'''

l = list(input("teste: "))

print(l)