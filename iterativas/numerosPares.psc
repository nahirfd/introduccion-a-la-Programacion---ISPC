Mostrar sólo los números pares desde 0 hasta el número ingresado (input). 
Nota: para saber si un número es par hacer i % 2 == 0)

Algoritmo MostrarNumerosPares
    Definir numero Como Entero
    Escribir "Ingrese un número:"
    Leer numero
    
    Para i <- 0 Hasta numero Con Paso 1 Hacer
        Si i MOD 2 = 0 Entonces
            Escribir i
        FinSi
    FinPara
FinAlgoritmo
