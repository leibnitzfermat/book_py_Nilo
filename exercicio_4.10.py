kwh = int(input("Qual a quantidade de kWh consumido: "))
tipo = input(
    "qual tipo de instalação, (R para residênciais, I para indústrias e C para comércios): ").upper()

if tipo == "R":
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "C":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "I":
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print("Erro!")


print(f"O valor a pagar é de R$ {kwh * preco:.2f}")
