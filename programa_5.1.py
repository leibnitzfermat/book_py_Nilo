# contagem de cédulas

valor = float(input("Digite o valor a pagar:"))
cedulas = 0
atual = 100
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    
    else:
        print(f"{cedulas} cédulas de R${atual}")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        if atual == 50:
            atual = 20
        if atual == 20:
            atual = 10
        if atual == 10:
            atual = 5
        if atual == 5:
            atual = 1
        if atual == 1:
            atual = 0.50
        if atual == 0.50:
            atual = 0.25
        if atual == 0.25:
            atual = 0.10
        if atual == 0.10:
            atual = 0.05
        if atual == 0.05:
            atual = 0.01
        cedulas = 0