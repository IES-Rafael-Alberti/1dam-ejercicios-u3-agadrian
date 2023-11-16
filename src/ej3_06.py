"""
Ejercicio 3.1.6

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""



def pedirAsignaturas(numeroAsignaturas: int) -> list:
    """
    Almacena en una lista las asignaturas introducidas

    Args
        numeroAsignaturas (int): cantidad de asignatuas que tengo que introducir

    Retorna:
            list: asignaturas introducidas
    """

    return list(input("Introduce asignatura: ") for _ in range(numeroAsignaturas))
    


def asignarNota(asignaturas: list) -> list:
    """
    Pide la nota para cada asignatura y la almacena en una lista dentro de la lista principal

    Args:
        asignaturas (list): lista de asignaturas
    
    Retorna:
        asignaturas (list): lista que contiene varias listas de cada asignatura y su nota
    """
    for i in range(len(asignaturas)):
        nota = input("Introduce nota (" + asignaturas[i] + "): ")
        asignaturas[i] = list((asignaturas[i],nota))

    return asignaturas



def ordenarNotas(asignaturasNotas: list) -> list:
    """
    Ordena de menor a mayor la lista, basandose en el segundo valor de cada sublista

    Args:
        asignaturasNotas (list): lista con sublistas de asignaturas y notas

    Retorna:
            listaOrdenada (list): la misma lista pero ordenada de menor a mayor nota
    """
    listaOrdenada = sorted(asignaturasNotas, key=lambda x: x[1])
    
    return listaOrdenada



def eliminarAprobadas(listaOrdenada: list) -> list:
    """
    Elimina las sublistas en una copia de la lista original cuyas notas sean >= 5

    Args:
        listaOrdenada (lista): lista ordenada

    Retorna:
            listaFinal (list): lista con las sublistas que tengan menos de un 5 de nota
    
    """
    listaFinal = listaOrdenada.copy()

    for i in range(len(listaOrdenada)):
        if int(listaOrdenada[i][1]) >= 5:
            listaFinal.pop()

    return listaFinal



def formatearLista(lista: list) -> str:
    """
    Formatea la lista para mostrarla mas legible

    Args: 
        lista (list): lista de valores a formatear
    
    Retorna:
            listaFormateada (str): los valores formateados de una forma mas legible, en cada linea un valor

    """
    listaFormateada = ""

    for i in range(len(lista)):
        listaFormateada += "\n" + str(lista[i][0]) + ": " + str(lista[i][1]) 
    
    return listaFormateada



def main():
    numeroAsignaturas = int(input("Cuantas asignaturas vas a introducir?: "))
    
    asignaturas = pedirAsignaturas(numeroAsignaturas)
    asignaturasNotas = asignarNota(asignaturas)
    listaOrdenada = ordenarNotas(asignaturasNotas)
    listaFinal = eliminarAprobadas(listaOrdenada)
    
    print("Debes repetir las asignaturas: " + formatearLista(listaFinal))



if __name__ == "__main__":
    main()