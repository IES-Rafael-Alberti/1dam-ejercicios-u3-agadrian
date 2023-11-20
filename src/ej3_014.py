"""
Ejercicio 3.2.1

Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""


def comprobarDivisa(diccionario: dict, divisa) -> bool:
    if divisa not in diccionario:
        return False
    else:
        return True



def main():
    diccionario = {'euro':'€', 'dollar':'$', 'yen':'¥'}
    divisa = input("Introduce divisa a comprobar: ").lower()
    
    if comprobarDivisa(diccionario, divisa):
        print(f"Tu divisa esta en el diccionario:  {diccionario[divisa]}")
    else:
        print("No esta en el diccionario")
    


if __name__ == "__main__":
    main()