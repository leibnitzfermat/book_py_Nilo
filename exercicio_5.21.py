# programa 5.1 - contagem de nota
while True:
    valor = float(input("Digite o valor a pagar:"))
    if valor == 0:
        break

    cedulas = 0
    atual = 100
    apagar = valor

    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1

        else:

            #print(f"{cedulas} cédulas de R${atual:5.2f}")
            print(
                f'{cedulas} { "cédula" if atual >= 2 else "moeda" } de R${atual:5.2f}')
            if apagar == 0:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 2
            elif atual == 2:
                atual = 1
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.25
            elif atual == 0.25:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.02
            elif atual == 0.02:
                atual = 0.01

            cedulas = 0
