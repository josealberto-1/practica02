def calificacion_final(calificaciones):
    practicas = [0.1, 0.1, 0.2, 0.3, 0.3]
    final = sum(calificacion * peso for calificacion,practicas in zip(calificaciones, practicas))
    if final >= 90:
        return (final, 'A')
    elif final >= 80:
        return (final, 'B')
    elif final >= 70:
        return (final, 'C')
    elif final >= 60:
        return (final, 'D')
    else:
        return (final, 'F')

nombre = input("Ingresa tu nombre: ")
print("Ingresa tus calificaciones en orden: tarea1, tarea2, examen parcial, examen final, proyecto")
calificaciones = list(map(float, input().split(",")))
final, literal = calificacion_final(calificaciones)
print("La calificación final de", nombre, "es", final, "con la literal", literal)
