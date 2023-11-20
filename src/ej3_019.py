"""
Ejercicio 3.2.6

Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

def mostrarDatos(diccionario:dict):
    print("\n** DATOS ACTUALIZADOS **")
    for k, v in diccionario.items():
        print(f"{k}: {v}")



def agregarDato(diccionario, clave, valor):
    diccionario[clave] = valor
    # Mostrar el diccionario cada vez que se agrege un dato
    mostrarDatos(diccionario)



def main():
    diccionario = {}

    nombre = input("\nNombre: ").capitalize()
    agregarDato(diccionario, "Nombre", nombre)
    
    edad = int(input("\nEdad: "))
    agregarDato(diccionario, "Edad", edad)
    
    sexo = input("\nSexo: ")
    agregarDato(diccionario, "Sexo", sexo)

    telefono = int(input("\nTelefono: "))
    agregarDato(diccionario, "Telefono", telefono)

    direccion = input("\nDireccion: ")
    agregarDato(diccionario, "Direccion", direccion)



if __name__ == "__main__":
    main()