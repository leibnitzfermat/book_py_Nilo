
deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
mensal = float(input("Depósito mensal: "))
mes = 1
saldo = deposito

while mes <= 12:

    saldo = saldo + (saldo * (taxa/100)) + mensal
    print(f'Saldo do mês {mes} e de R${saldo:5.2f}.')
    mes += 1
print(f"O ganho obtido com os juros fi de R${saldo - deposito:8.2f}")

'''
# para manutenção, no mes 2 pedir qual valor sera depositado e mostra quando vai rende
deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))

mes = 1
saldo = deposito
rendimento = 0

while mes <= 12:
    mensal = float(input(f"Depósito previsto para o mês {mes}: "))
    saldo = saldo + (saldo * (taxa/100)) + mensal
    rendimento = rendimento + (saldo * taxa/100)
    print(f'Saldo do mês {mes} e de R${saldo:5.2f}.')
    print(f'Rendimento do mês {mes} e de R${rendimento:.2f}')
    mes += 1
print(f"O ganho obtido com os juros fi de R${saldo - deposito:8.2f}")
'''
