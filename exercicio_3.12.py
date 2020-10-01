distância = float(input("Digite a distância em km: "))
velocidade_media = float(input("Digite a velocidade média em km/h: "))
tempo = distância / velocidade_media
print(f"O tempo estimado é de {tempo:5.2f} horas")
# Opcional: imprimir o tempo em horas, minutos e segundos
tempo_s = int(tempo * 3600) # convertemos de horas para segundos
horas = int(tempo_s / 3600) # parte inteira
tempo_s = int(tempo_s % 3600) # o resto
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)
print(f"{horas}:{minutos}:{segundos}")
print("%05d:%02d:%02d" % (horas, minutos, segundos))