def fibonacci_hasta(n):
    fib = []
    a, b = 0, 1
    while a <= n:
        fib.append(a)
        a, b = b, a + b 
    return fib
serie_fibonacci = fibonacci_hasta(50)
print(f"La serie de Fibonacci entre 0 y 50 es: {serie_fibonacci}")
