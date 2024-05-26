#Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 

nombres_unicos = []

print("Ingrese 10 nombres de personas únicos:")

while len(nombres_unicos) < 10:
    nombre = input(f"Ingrese el nombre de la persona {len(nombres_unicos) + 1}: ")

    if nombre in nombres_unicos:
        print("Ese nombre ya ha sido ingresado. Por favor, ingrese un nombre diferente.")
    else:
        nombres_unicos.append(nombre)

print("\nLos nombres ingresados son: ")
for nombre in nombres_unicos:
    print(nombre)
