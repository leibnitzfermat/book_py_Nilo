def mdc(a, b):
    if b == 0:
        return a
    elif a > b:
        return mdc(b, a % b)
    
print(f"MDC 32 e 24 --> {mdc(32, 24)}")
print(f"MDC 5 e 3 -->   {mdc(5, 3)}")