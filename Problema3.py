numeros = []
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    if respuesta == 'no':
        break  
    if respuesta == 'si':
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
pares = len([num for num in numeros if num % 2 == 0])
impares = len([num for num in numeros if num % 2 != 0])
print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
