#En un nuevo diccionario llamado familia guardar 4 personas, 
#cada una de ellas con los mismos 5 datos (
#nombre, apellido, dni, email, fecha de nacimiento)

for i in range (4):
    nombre = input("Ingrese su nombre")
    apellido = input("Ingrese su apellido")
    dni = input("Ingrese su dni")
    email = input("Ingrese su email")
    fechaNacimiento =input("Ingrese su fecha de nacimiento")

familia = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'email': email,
        'fecha nacimiento': fechaNacimiento
}

print(familia)