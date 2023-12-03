"""
Ejercicio 3.1.4

Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

def introducirNumeros() -> int:
    """
    Pide un numero hasta que sea valido (1-49 incluido)

    Retorna:
        int del numero introducido
    """
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



def listaNumeros() -> list:
    """
    Pide numeros y crea una lista con los numeros introducidos

    Retorna:
            list: de los numeros ontroducidos
    """
    lista = []

    while len(lista) < 6:
        lista.append(introducirNumeros())
    
    lista.sort()
    
    return lista



def pedirReintegro() -> int:
    """
    Pide un numero hasta que sea valido (1-9 incluido)

    Retorna:
            int del numero introducido
    """
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



def mostrarListaFormateada(lista:list) -> str:
    """
    Crea un string mas legible a partir de una lista

    Args:
        list: lista con valores

    Retorna:
            str de los valores de la lista separados por coma 
    """
    listaFormateada = ""
    
    listaFormateada += ", ".join(str(i) for i in lista)

    return listaFormateada



def main():
    print("Introduce numeros: ")
    lista = listaNumeros()

    print("Introduce reintegro: ")
    reintegro = pedirReintegro()

    lista.append(reintegro)
    
    print("Numeros ordenados y reintegro: " + mostrarListaFormateada(lista))



if __name__ == "__main__":
    main()