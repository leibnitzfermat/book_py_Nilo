velo = float(input("Qual foi a velocidade do seu carro? "))
if velo > 80:
    print(f"Você foi multado em R${(velo - 80) * 5 :.2f} por ultapassa {velo - 80}km da velocidade permitida!")
else:
    print("Velocidade dentro do limite, boa viagem!")