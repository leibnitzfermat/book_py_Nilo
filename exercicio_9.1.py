import sys

nome = sys.argv[1]
arquivo = open(nome, "r")
for linha in arquivo.readlines():
    print(linha)