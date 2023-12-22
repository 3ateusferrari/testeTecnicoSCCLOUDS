# Resolução usando função recursiva
def fibonacciRecursiva(n):
    if n < 0:
        return False
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fibonacciRecursiva(3))

def fibonacci_linear(n):
    if n < 0:
        return False
    if n == 0:
        return 0
    a = 0
    b = 1
    for _ in range(1, n):
        a, b = b, a + b
    return b