quanti = int(input("Qual a quantidade de cigarros que fuma por dia? "))
anos = float(input("Quantos anos fuma? "))

quanti_minuto = quanti * 10
anos_minuto = anos * 365
dias = (quanti_minuto * anos_minuto) / 1440
print(dias)

# minuto em dia = divida o valor de tempo por 1440