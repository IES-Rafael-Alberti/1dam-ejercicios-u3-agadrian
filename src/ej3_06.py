"""
Ejercicio 3.1.6

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""


def pedirAsignaturas(numeroAsignaturas):
    tuplaAsignaturas = tuple(input("Introduce asignatura: ") for _ in range(numeroAsignaturas))
    
    return tuplaAsignaturas
    



def main():
    numeroAsignaturas = int(input("Cuantas asignaturas vas a introducir?: "))
    print(pedirAsignaturas(numeroAsignaturas))

    

if __name__ == "__main__":
    main()