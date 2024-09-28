def convertir_fecha(fecha):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    if "/" in fecha:
        mes, dia, anio = fecha.split("/")
        return f"{anio}-{int(mes):02}-{int(dia):02}"
    else:
        partes = fecha.replace(",", "").split()
        mes_texto, dia, anio = partes
        mes_numero = meses.index(mes_texto) + 1
        return f"{anio}-{mes_numero:02}-{int(dia):02}"
fecha = input("Ingrese una fecha (MM/DD/AAAA o Mes día, año): ")
print("Fecha en formato AAAA-MM-DD:", convertir_fecha(fecha))
