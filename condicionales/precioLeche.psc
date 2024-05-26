Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados. 
La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). 
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

Proceso PrecioLeche
    Definir cantidad, precio_unitario, costo, es_jubilado Como Real
    precio_unitario <- 1000
    Escribir "Ingrese la cantidad de leche comprada:"
    Leer cantidad
    Escribir "¿Es el cliente jubilado? (1 para sí, 0 para no):"
    Leer es_jubilado
    
    costo <- cantidad * precio_unitario
    
    Si cantidad > 12 Y cantidad <= 24 Entonces
        costo <- costo * 0.90
    FinSi
    
    Si cantidad > 24 Entonces
        costo <- costo * 0.85
    FinSi
    
    Si es_jubilado = 1 Entonces
        costo <- costo * 0.90
    FinSi
    
    Escribir "El total a pagar es: ", costo
FinProceso