def soma(l):
    total = 0
    x = 0
    for e in l:
        total += e
    return total
l = [1, 7, 2, 9,15]
print(soma(l))
print(soma([1,2,3,4,5,6,7,8,9,0]))