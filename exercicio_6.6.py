ultimo = 10
fila1 = list(range(1, ultimo + 1))
fila2 = list(range(1, ultimo + 1))
while True:

    print(f'''\nExistem {len(fila1)} clientes na fila 1
          Fila ataul: {fila1}
          \nExistem {len(fila2)} clientes na fila 2
          Fila ataul: {fila2}
          \nDigite A para adicionar um cliente ao fim da fila 1
          ou B para a fila 2, ou F para realizar o atendimento
          na fila 1 ou G para realizar na fila 2. S para sair.''')
    
    operacao = input("Operação (A, B, F, G ou S): ").upper()
    x = 0
    
    sair = False
    while x < len(operacao):
        if operacao[x] == "F":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f'Cliente {atendido} atendido.')
            else:
                print('Fila vazia! Ninguém para atender.')
        elif operacao[x] == "G":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f'Cliente {atendido} atendido.')
            else:
                print('Fila vazia! Ninguém para atender.')
        elif operacao[x] == "A":
            ultimo += 1
            fila1.append(ultimo)
        elif operacao[x] == "B":
            ultimo += 1
            fila2.append(ultimo)
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print('Operação invalida! Digite apenas F, A ou S!')
        x += 1
    if (sair):
        break
    