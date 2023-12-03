"""
Ejercicio 3.2.2

Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""


def pedirDatos():

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    direccion = input("Direccion: ")
    telefono = int(input("Telefono: "))

    datos = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}

    return datos



def main():
    print("Introduce tus datos: ")
    datos = pedirDatos()

    print(f"{datos['nombre'].capitalize()} tiene {datos['edad']} años, vive en {datos['direccion']} y su numero de telefono es {datos['telefono']}.")



if __name__ == "__main__":
    main()