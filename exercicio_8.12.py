def teste(s, l):
    # a linha abaixo já faz verificação booleana
    return s in l
    
   
#    if s in l:
#        return True
#    else:
#        return False
    
l = [1, 3, 5, 6, 9]


print(teste(1, l))
print(teste(2, l))
print(teste(3, l))
print(teste(5, l))