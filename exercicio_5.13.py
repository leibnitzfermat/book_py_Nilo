divida = float(input("Valor inicial da divida: "))
taxa = float(input("Juros mensal: "))
pagamento = float(input("Pagamento mensal: "))

mes = 1

if (divida * (taxa/100) > pagamento):
    print("Sua divida é impagavel, juros maior que o pagamento mensal.")

else:
    saldo = divida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa/100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print(f"Saldo da dívida no mês {mes} é de R${saldo:.2f}.")
        mes += 1
    print(f"Para pagar uma dívida de R${divida:.2f}, a {taxa:.2f}%  de juros,")
    print(
        f"você precisará de {mes - 1} meses, pagando um total de R${juros_pago:.2f} de juros.")
    print(
        f"No último mês, você teria um saldo residual de R${saldo:.2f} a pagar.")
