EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada
materia y quiere saber cuál es su promedio.

Algoritmo PromedioNotas
	Definir nota1, nota2, nota3, nota4, nota5, promedio Como Real;

	Escribir "Ingrese la nota de la primera materia:";
	Leer nota1;
	Escribir "Ingrese la nota de la segunda materia:";
	Leer nota2;
	Escribir "Ingrese la nota de la tercera materia:";
	Leer nota3;
	Escribir "Ingrese la nota de la cuarta materia:";
	Leer nota4;
	Escribir "Ingrese la nota de la quinta materia:";
	Leer nota5;

	promedio <- (nota1 + nota2 + nota3 + nota4 + nota5) / 5;

	Escribir "El promedio de las notas es: ", promedio;
FinAlgoritmo
