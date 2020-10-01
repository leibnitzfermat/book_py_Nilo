
deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))

mes = 1
saldo = deposito

while mes <= 24:
    saldo = saldo + (saldo * (taxa/100))
    print(f'Saldo do mês {mes} e de R${saldo:5.2f}.')
    mes += 1
print(f"O ganho obtido com os juros fi de R${saldo - deposito:8.2f}")

'''

deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))

mes = 1
saldo = deposito
rendimeto = 0

while mes <= 24:
    rendimento = rendimeto + (saldo * taxa/100)
    saldo = saldo + (saldo * (taxa/100))
    print(f'Saldo do mês {mes} e de R${saldo:5.2f}.')
    print(f'Rendimento do mês {mes} e de R${rendimento:5.2f}.')
    mes += 1
print(f"O ganho obtido com os juros fi de R${saldo - deposito:8.2f}")
'''
