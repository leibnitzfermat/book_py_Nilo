primeiro = input("1ª string: ")

segunda = input("2ª string: ")

terceira = ""

for letra in primeiro:
    if letra not in segunda and letra not in terceira:
        terceira += letra

for letra in segunda:
    if letra not in primeiro and letra not in terceira:
        terceira += letra

if terceira == "":
    print("Nada")

else:
    print(f'Resultado: {terceira}')
    
