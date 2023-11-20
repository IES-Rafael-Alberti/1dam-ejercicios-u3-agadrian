"""
Ejercicio 3.2.7

Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""


def añadirArticulos(listaCompra: dict) -> dict:
    ok = False

    while not ok:
        articulo = input("Introduce articulo (enter para acabar): ")
        if articulo == "":
            ok = True
        else:
            precio = float(input("Precio del articulo: "))
            listaCompra[articulo] = precio
    
    return listaCompra
     


def mostrarLista(listaCompra:dict):
    total = 0
    print("\nLista de la compra")
    for k,v in listaCompra.items():
        print(f"{k}: {v}€")
        total += v
    print(f"\nTotal compra: {total}€")



def main():
    listaCompra = {}
    añadirArticulos(listaCompra)
    mostrarLista(listaCompra)



if __name__ == "__main__":
    main()