primeiro = input("1ª string: ")

segunda = input("2ª string: ")

terceira = ""

for letra in primeiro:
    if letra not in segunda:
        terceira += letra

if terceira == "":
    print("Nada")

else:
    print(f'Resultado: {terceira}')