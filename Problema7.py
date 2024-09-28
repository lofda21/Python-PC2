def encontrar_numeros_perfectos(limite):
    def divisores_propios(n):
        divisores = []
        for i in range(1, n):
            if n % i == 0:
                divisores.append(i)
        return divisores
    numeros_perfectos = []
    for num in range(2, limite):
        if sum(divisores_propios(num)) == num:
            numeros_perfectos.append(num)
    return numeros_perfectos
limite = 1000
numeros_perfectos = encontrar_numeros_perfectos(limite)
print("Números perfectos menores que 1000:", numeros_perfectos)
