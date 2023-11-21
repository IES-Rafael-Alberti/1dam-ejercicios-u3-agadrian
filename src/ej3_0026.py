"""
Ejercicio 3.3.2

Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.

"""


def pedirNombres() -> set:
    ok = False
    nombres = set()
    while not ok:
        nombre = input("Nombre: ")
        if nombre == 'x':
            ok = True
        else:
            nombres.add(nombre)
    
    return nombres



def mostrarNombresUnicos(nombresPrimaria:set, nombresSecundaria:set):
    
    print(nombresPrimaria | nombresSecundaria)
    


def mostrarNombresRepetidos(nombresPrimaria:set, nombresSecundaria:set):

    print(nombresPrimaria & nombresSecundaria)



def mostrarPrimariaNoSecundaria(nombresPrimaria:set, nombresSecundaria:set):

    print(nombresPrimaria - nombresSecundaria)



def mostrarPrimariaEnSecundaria(nombresPrimaria:set, nombresSecundaria:set):
    nombresPrimaria.issubset(nombresSecundaria)
    


def main():
    print("Introduce nombres alumnos primaria (x para acabar): ")
    nombresPrimaria = pedirNombres()

    print("Introduce nombres alumnos secundaria (x para acabar): ")
    nombresSecundaria = pedirNombres()

    mostrarNombresUnicos(nombresPrimaria, nombresSecundaria)
    mostrarNombresRepetidos(nombresPrimaria, nombresSecundaria)
    mostrarPrimariaNoSecundaria(nombresPrimaria, nombresSecundaria)
    mostrarPrimariaEnSecundaria(nombresPrimaria, nombresSecundaria)


if __name__ == "__main__":
    main()
