apagar = 0
while True:
    cod = int(input('Digite o codigo do produto que deseja: '))
    preco = 0
    if cod == 0:
        break
    elif cod == 1:
        preco = 0.50
    elif cod == 2:
        preco = 1.00
    elif cod == 3:
        preco = 4.00
    elif cod == 5:
        preco = 7.00
    elif cod == 9:
        preco = 8.00
    else:
        print("Codigo errado!")
    if preco != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (preco * quantidade)
print(f'Total a paga pelos iten(s) é de R$ {apagar:8.2f}')
