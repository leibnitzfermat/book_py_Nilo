def fib(x):
    p = 0
    n = 1
    while x > 0:
        p, n = n, p + n
        n -= 1
        
    return p

for x in range(100):
    print(f"Fibonacci({x}) = {fib(x)}") 
        