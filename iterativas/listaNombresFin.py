#Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”

nombres = []

nombre = input("Ingrese un nombre (o escriba 'fin' para terminar): ")
while nombre.lower() != 'fin':
    nombres.append(nombre)
    nombre = input("Ingrese otro nombre (o escriba 'fin' para terminar): ")


print("Los nombres ingresados son:")
for nombre in nombres:
    print(nombre)
