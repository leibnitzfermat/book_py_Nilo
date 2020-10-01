#l = [2,5,1,50,7]
#
#a = l[::-1]
#
#print(a)
#
##metodo que organiza a lista em questão em ordem crescente output [1,2,5,7,50]
#l.sort()
#
#print(l)
#
#
#
#l = {'a':2, 'b':3, 'c':4, 'd':5}
#
#print(l.values())

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "feijão": 1.50}

while True:
    produto = input("Digite o nome do produto, fim para terminar:")
    if produto == "fim":
        break
    
    if produto in tabela:
        print(f"Preço {tabela[produto]:5.2f}")
        
    else:
        print("Produto não encotrado")
        
