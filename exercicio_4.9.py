valor = float(input("Valor da casa: "))
salario = float(input("Seu salário: "))
anos = int(input("Quantidade de anos a pagar: "))
mes = anos * 12
prestacao = valor / mes
if prestacao > salario * 0.3:
    print("infelizmente não pode obter emprestimo")
else:
    print(f"Emprestimo aprovado, valor da parcela: R${prestacao:.2f}")
