# Estructura de datos inicial 
Datos = {
    "Alumnos": [
        {
            "Nombre": "Juan",
            "Apellido": "Perez",
            "DNI": "12345678",
            "Fecha de nacimiento": "01/01/2000",
            "Tutor": "Maria Perez",
            "Notas": [7, 8, 9],
            "Faltas": 2,
            "amonestaciones": 1
        },
        {
            "Nombre": "Maria",
            "Apellido": "Gomez",
            "DNI": "87654321",
            "Fecha de nacimiento": "05/05/2001",
            "Tutor": "Carlos Gomez",
            "Notas": [6, 8, 7],
            "Faltas": 3,
            "amonestaciones": 2
        },
        {
            "Nombre": "Pedro",
            "Apellido": "Rodriguez",
            "DNI": "23456789",
            "Fecha de nacimiento": "10/10/1999",
            "Tutor": "Laura Rodriguez",
            "Notas": [9, 9, 8],
            "Faltas": 1,
            "amonestaciones": 0
        },
        {
            "Nombre": "Ana",
            "Apellido": "Garcia",
            "DNI": "98765432",
            "Fecha de nacimiento": "15/03/2002",
            "Tutor": "David Garcia",
            "Notas": [8, 7, 6],
            "Faltas": 4,
            "amonestaciones": 3
        },
        {
            "Nombre": "Carlos",
            "Apellido": "Bush",
            "DNI": "34567890",
            "Fecha de nacimiento": "20/07/2003",
            "Tutor": "Elena Bush",
            "Notas": [7, 6, 8],
            "Faltas": 0,
            "amonestaciones": 0
        }
    ]
}

# Funcion para agregar un nuevo alumno
def agregar_alumno(datos, alumno):
    datos["Alumnos"].append(alumno)

# Funcion para expulsar un alumno
def expulsar_alumno(datos, dni):
    alumnos = datos["Alumnos"]
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            alumnos.remove(alumno)
            print(f"Alumno con DNI {dni} expulsado.")
            break
    else:
        print(f"No se encontro ningun alumno con DNI {dni}.")

# Funcion para mostrar los datos de un alumno 
def mostrar_datos_alumno(datos, dni):
    alumnos = datos["Alumnos"]
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            print("\nDatos del alumno:")
            for clave, valor in alumno.items():
                print(f"{clave}: {valor}")
            break
    else:
        print(f"No se encontro ningun alumno con DNI {dni}.")

# Funcion para modificar los datos de un alumno
def modificar_datos_alumno(datos, dni, campo, nuevo_valor):
    alumnos = datos["Alumnos"]
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            if campo in alumno:
                alumno[campo] = nuevo_valor
                print(f"Dato {campo} modificado exitosamente.")
                break
            else:
                print(f"No existe el campo {campo} en los datos del alumno.")
                break
    else:
        print(f"No se encontro ningun alumno con DNI {dni}.")

# Funcion para mostrar la lista de todos los alumnos
def mostrar_lista_alumnos(datos):
    print("\nLista de alumnos:")
    for alumno in datos["Alumnos"]:
        print(f"{alumno['Nombre']} {alumno['Apellido']} - DNI: {alumno['DNI']}")

# Funcion para agregar un nuevo alumno
def agregar_alumno(datos, nuevo_alumno):
    datos["Alumnos"].append(nuevo_alumno)
    print("Alumno agregado correctamente.")

# Funcion para expulsar un alumno
def expulsar_alumno(datos, dni):
    alumnos = datos["Alumnos"]
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            alumnos.remove(alumno)
            print(f"Alumno con DNI {dni} expulsado.")
            break
    else:
        print(f"No se encontro ningun alumno con DNI {dni}.")

# Funcion principal (menu).
def menu_principal(datos):
    while True:
        print("\n=== Menu Principal ===")
        print("1. Mostrar datos de un alumno")
        print("2. Modificar datos de un alumno")
        print("3. Mostrar lista de alumnos")
        print("4. Agregar nuevo alumno")
        print("5. Expulsar alumno")
        print("6. Salir")
        opcion = input("Ingrese el numero de la opcion que desea realizar: ")

        if opcion == "1":
            dni = input("Ingrese el DNI del alumno: ")
            mostrar_datos_alumno(datos, dni)
        elif opcion == "2":
            dni = input("Ingrese el DNI del alumno: ")
            campo = input("Ingrese el campo que desea modificar: ")
            nuevo_valor = input("Ingrese el nuevo valor: ")
            modificar_datos_alumno(datos, dni, campo, nuevo_valor)
        elif opcion == "3":
            mostrar_lista_alumnos(datos)
        elif opcion == "4":
            nuevo_alumno = {
                "Nombre": input("Nombre: "),
                "Apellido": input("Apellido: "),
                "DNI": input("DNI: "),
                "Fecha de nacimiento": input("Fecha de nacimiento (DD/MM/AAAA): "),
                "Tutor": input("Nombre del tutor: "),
                "Notas": [int(nota.strip()) for nota in input("Notas (separadas por comas): ").split(",")],
                "Faltas": int(input("Cantidad de faltas: ")),
                "amonestaciones": int(input("Cantidad de amonestaciones: "))
            }
            agregar_alumno(datos, nuevo_alumno)
        elif opcion == "5":
            dni = input("Ingrese el DNI del alumno a expulsar: ")
            expulsar_alumno(datos, dni)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Por favor, ingrese un numero del 1 al 6.")

# Ejecutar el programa
menu_principal(Datos)
