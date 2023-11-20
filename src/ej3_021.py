"""
Ejercicio 3.2.8

Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""


def crearDiccionario(palabras:str) -> dict:

    diccionario = dict((par.split(":") for par in palabras.split(",")))

    return diccionario


def traducirFrase(frase:str, diccionario:dict):
    palabras = frase.split(' ')

    for palabra in palabras:
        for i in diccionario:
            if palabra == i:
                palabras.replace(palabra, diccionario.get(diccionario[i]))
                
    return palabras
        




def main():
    palabras = input("Introduce palabras español a ingles en formato <palabra>:<traducción>,<palabra>:<traducción>,...: ")
    diccionario = crearDiccionario(palabras)

    frase = input("Introduce frase a traducir: ")
    print(traducirFrase(frase, diccionario))






if __name__ == "__main__":
    main()