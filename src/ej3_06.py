"""
Ejercicio 3.1.6

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""


def pedirAsignaturas(numeroAsignaturas):

    return list(input("Introduce asignatura: ") for _ in range(numeroAsignaturas))
    

def asignarNota(asignaturas):

    for i in range(len(asignaturas)):
        nota = input("Introduce nota (" + asignaturas[i] + "): ")
        asignaturas[i] = list((asignaturas[i],nota))

    return asignaturas

def oredenarNotas(asignaturas):

    #asignaturas[i][1]

def main():
    numeroAsignaturas = int(input("Cuantas asignaturas vas a introducir?: "))
    asignaturas = pedirAsignaturas(numeroAsignaturas)
    asignaturasNotas = asignarNota(asignaturas)
    print(asignaturasNotas)
    print(asignaturasNotas.sort())

# (["matematicas", 2],["lengua",3]) o

if __name__ == "__main__":
    main()