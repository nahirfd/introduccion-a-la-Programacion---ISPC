EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo
que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
cliente le indica que necesita conocer el costo de mano de obra para pintar una
pared rectangular de un galpón. El pintor cobra un monto fijo por cada metro
cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
pintar la pared.

Algoritmo CostoPintura
	Definir largo, ancho, precioPorMetro, area, costo Como Real;

	Escribir "Ingrese el largo de la pared (en metros):";
	Leer largo;
	Escribir "Ingrese el ancho de la pared (en metros):";
	Leer ancho;
	Escribir "Ingrese el precio de mano de obra por metro cuadrado:";
	Leer precioPorMetro;

	area <- largo * ancho;
	costo <- area * precioPorMetro;

	Escribir "El costo de mano de obra para pintar la pared es: $", costo;
FinAlgoritmo