# Um minuto tem 60 segundos
# Uma hora tem 3600 (60 * 60) segundos
# Um dia tem 24 horas, logo 24 * 3600 segundos

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

total = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos

print(f"Convertido em segundo é igual a {total} segundos.")
