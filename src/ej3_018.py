"""
Ejercicio 3.2.5

Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""



def mostrarCreditos(creditos):
    total = 0
    for asignatura, credito in creditos.items():
        print(f"{asignatura} tiene {credito} creditos")
        total += credito
    print(f"En total tienes: {total} creditos")



def main():
    creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    mostrarCreditos(creditos)



if __name__ == "__main__":
    main()