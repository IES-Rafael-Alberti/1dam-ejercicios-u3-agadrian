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

def oredenarNotas(asignaturasNotas):
    listaOrdenada = sorted(asignaturasNotas, key=lambda x: x[1])
    
    return listaOrdenada

def eliminarAprobadas(listaOrdenada):
    listaFinal = listaOrdenada.copy()
    for i in range(len(listaOrdenada)):
        if int(listaOrdenada[i][1]) >= 5:
            listaFinal.pop()
    return listaFinal


def main():
    numeroAsignaturas = int(input("Cuantas asignaturas vas a introducir?: "))
    
    asignaturas = pedirAsignaturas(numeroAsignaturas)
    asignaturasNotas = asignarNota(asignaturas)
    listaOrdenada = oredenarNotas(asignaturasNotas)
    listaFinal = eliminarAprobadas(listaOrdenada)
    
    print("Debes repetir las asignaturas: " + str(listaFinal))


if __name__ == "__main__":
    main()