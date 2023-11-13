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
                raise NameError("error")
            ok = True
        except NameError:
            print("Numero ha de estar entre 1-49 incluidos")
        except Exception:
            print("Debe ser un valor numerico")
   
    return int(numero)



def pedirReintegro():
    ok = False
    while not ok:
        try:
            reintegro = int("Introduce reintegro: ")
            if reintegro < 1 or reintegro > 9:
                raise ValueError ("Numero incorrecto (1-9)")
            ok = True
        except ValueError:
            print("ERROR")



def listaNumeros():
    lista = []

    while len(lista) < 6:
        lista.append(introducirNumeros())
    
    return lista



def main():
    
    print("Introduce numeros")

    print(listaNumeros())




if __name__ == "__main__":
    main()