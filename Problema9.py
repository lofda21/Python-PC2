def omitir_vocales(cadena):
    vocales = "aeiouAEIOU"
    resultado = ""
    for caracter in cadena:
        if caracter not in vocales:
            resultado += caracter
    return resultado
texto = input("Ingrese una cadena de texto: ")
print("Texto sin vocales:", omitir_vocales(texto))