materia_1 = float(input("Digite sua nota 1º: "))
materia_2 = float(input("Digite sua nota 2º: "))
materia_3 = float(input("Digite sua nota 3º: "))
x = (materia_1 + materia_2 + materia_3) / 3
if x >= 7:
    print("aprovado")
else:
    print("reprovado")
