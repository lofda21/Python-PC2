alumnos = []
while True:
    nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ").strip()
    if nombre.lower() == 'salir':
        break  
    notas = []
    for i in range(1, 4):
        calificacion = float(input(f"Ingrese la calificación {i}: "))
        notas.append(calificacion)
    alumno = {
        'Alumno': nombre,
        'Notas': notas
    }
    alumnos.append(alumno)
print("Listado completo de alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
