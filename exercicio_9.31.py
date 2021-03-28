from os import path

a = input("qual diretorio que verificar?: ")
if path.exists(a):
    print("O diretorio z existe.")
    if path.isdir(a):
        print("e um diretorio")
else: print("não existe")