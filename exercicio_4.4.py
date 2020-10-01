salario = float(input("Digite seu salário: "))
if salario > 1250:
    print(f"Seu salário tera um aumento de: R${salario * 10/100:.2f}")
if salario < 1250:
    print(f"Seu salário tera um aumento de: R${salario * 15/100:.2f}")
