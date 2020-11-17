def verificacso(s, minimo, maximo):
    tamanho = len(s)
    return minimo <= tamanho <= maximo


print(verificacso("", 1, 5))
print(verificacso("ABC", 2, 5))
print(verificacso("ABCEFG", 3, 5))
print(verificacso("ABCEFG", 1, 10))
