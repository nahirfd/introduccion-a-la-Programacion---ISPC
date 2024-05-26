""" En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas 
(las notas van de 0 a 10) de los alumnos de un curso. Se necesita saber si el rendimiento ha sido elevado 
(el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). 
Desarrollar un algoritmo que resuelva este problema. 
Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen. """


def rendimientoAlumnos(promedio):
    if promedio > 8:
        return print('elevado')
    elif 6 <= promedio <= 8:
        return print('aceptable')
    else:
        return print('bajo')


cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes que rindieron el examen: "))


notas = []


for i in range(cantidad_estudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {i + 1} (entre 0 y 10): "))
    while nota < 0 or nota > 10:
        print("Nota inválida. Debe ser un valor entre 0 y 10.")
        nota = float(input(f"Ingrese la nota del estudiante {i + 1} (entre 0 y 10): "))
    notas.append(nota)


promedio_notas = sum(notas) / cantidad_estudiantes


rendimiento = rendimientoAlumnos(promedio_notas)


print(f"El promedio de notas del curso es: {promedio_notas:.2f}")
print(f"El rendimiento del curso ha sido: {rendimiento}")
