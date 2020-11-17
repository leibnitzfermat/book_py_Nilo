import random

a = random.randint(1, 10)

te = 0

while te < 3:
    x = int(input("Digite um numero entre 1 e 10: "))
    
    if a == x:
        print("Acertou")
        break
    else:
        print("Errou")
    te += 1