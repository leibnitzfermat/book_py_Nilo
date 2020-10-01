
a = "teste"

def f():
    global a
    a = 123
    print(a)
    
print(a)

f()
