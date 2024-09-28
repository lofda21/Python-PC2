def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def suma_primos_hasta_n(n):
    suma = 0
    for num in range(n):
        if es_primo(num):
            suma += num
    return suma
resultado = suma_primos_hasta_n(100)
print(f"La suma de todos los números primos menores que 100 es: {resultado}")
