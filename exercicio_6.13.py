
t = [-10, -8, 0, 1, 2, 5, -2, -4]

maximo = t[0]
for e in t:
    if e > maximo:
        maximo = e
print(f'A maior temperatura é: {maximo}')

menor = t[0]
for e in t:
    if e < menor:
        menor = e
print(f'A menor temperatura é: {menor}')

m = 0
for media in t:
    m = m + media
print(f'A temperatura média é {m/len(t)}')

####################################################33

t = [-10, -8, 0, 1, 2, 5, -2, -4]

print(f'A maior temperatura é:', max(t))

print(f'A maior temperatura é:{min(t)}')

print(f'A temperatura média é:{sum(t)/len(t)}')
