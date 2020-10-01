ANTES = [1, 2, 5, 6, 9]
DEPOIS = [1, 2, 8, 10]

conjunto_antes = set(ANTES)
conjunto_depois = set(DEPOIS)

# Conjuntos suportam o operador & para realizar a interseção, ou seja,
# A & B resulta no conjunto de elementos presentes em A e B
print("Antes:", ANTES)
print("Depois:", DEPOIS)
print("Elementos que não mudaram: ", conjunto_antes & conjunto_depois)  #1,2
print("Elementos novos", conjunto_depois - conjunto_antes)  #8,10
print("Elementos que foram removidos", conjunto_antes - conjunto_depois)    #5,6,9