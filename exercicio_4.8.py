a = float(input("Primeiro numero: "))
b = float(input("Segundo numero: "))
operacao = input("digite a operação que deseja fazer (+, -, * ou /): ")

if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 'Refaça a operação'
print(f"Resultado:{resultado:.1f}")
