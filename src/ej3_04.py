"""
Ejercicio 3.1.4

Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

def introducirNumeros():
    ok = False
    while not ok:
        try:    
            numero = int(input(""))
            if numero < 1 or numero > 49:
                raise TypeError("Error - debe introducir un numero dentro del rango 1-49 incluidos")
            ok = True
        except TypeError as e:
            print(str(e))
        except Exception:
            print("Debe introducir un valor numerico")
   
    return int(numero)



def listaNumeros():
    lista = []

    while len(lista) < 6:
        lista.append(introducirNumeros())
    
    lista.sort()
    
    return lista



def pedirReintegro():
    ok = False
    while not ok:
        try:
            reintegro = int(input(""))
            if reintegro < 1 or reintegro > 9:
                raise TypeError ("Error - debe introducir un numero dentro del rango 1-9 incluidos")
            ok = True
        except TypeError as e:
            print(str(e))
        except Exception:
            print("Debe introducir un valor numerico")

    return int(reintegro)



def mostrarLista(lista):
    listaFormateada = ""

    for i in lista:
        listaFormateada += ", ".join(str(i))

    return listaFormateada


def main():
    
    print("Introduce numeros: ")
    lista = listaNumeros()

    print("Introduce reintegro: ")
    reintegro = pedirReintegro()

    lista.append(reintegro)

    print("Numeros ordenados y reintegro: " + ", ".join(mostrarLista(lista)))



if __name__ == "__main__":
    main()