l = []
while True:
    n = int(input('Digite um número (0 sai): '))
    if n == 0:
        break
    l.append(n)
for i in l:     #nem todos while poder ser substituido por for, while é indicador para repetições nas quais
    print(i)    #não sabemos ainda quantas vezes vamos repetir ou onde manipulamos os indices de forma não
                #sequencial.