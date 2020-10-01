preco = float(input("Qual o preço: "))
desconto = float(input("Qual desconto: "))

print(f"Seu desconto foi de R$ {preco * desconto / 100} e o total a pagar R$ {preco - preco * desconto / 100}.")
