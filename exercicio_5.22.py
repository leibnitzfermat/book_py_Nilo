while True:

    n = int(input("tabuada de: "))
    o = input(
        "Adição(+)\nSubtração(-)\nDivisão(/)\nMultiplicação(*)\nSair(5)\nOperação: ")
    if o == "5":
        break
    x = 0
    while x <= 10:
        if o == "+":
            print(f'{n} + {x} = {n+x}')
            x += 1
        elif o == "-":
            print(f'{n} - {x} = {n-x}')
            x += 1
        elif o == "/":
            print(f'{n} / {x} = {n/x:.2f}')
            x += 1
        elif o == "*":
            print(f'{n} * {x} = {n*x}')
            x += 1
