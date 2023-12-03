"""
Ejercicio 3.2.8

Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

def crearDiccionario(palabras:str) -> dict:

    # Hace split de (,) y crea una lista de pares de valores ["esp:ing", "esp:ing"]. Luego hace split de (:), y añade este split a una lista, quedaria una lista con varias listas de pares dentro [["esp","ing"], ["esp","ing"]] y por ultimo lo convierte a diccionario, que resulta en el return de la funcion
    diccionario = dict((par.split(":") for par in palabras.split(",")))

    return diccionario



#hola:hello,adios:bye,bienvenido:yourwelcome
def traducirFrase(frase:str, diccionario:dict):
    palabras = frase.split(" ")
    traducido = []

    for palabra in palabras:
        # Si esxite palabra, devuelve su valor e ignora la segunda variable palabra dentro del get. Si no, devuleve esta segunda variable, que devolveria el mismo valor
        traducido.append(diccionario.get(palabra,palabra))

    fraseFinal = " ".join(traducido)

    return fraseFinal

    

def main():
    palabras = input("Introduce palabras español a ingles en formato <palabra>:<traducción>,<palabra2>:<traducción2> : ")
    diccionario = crearDiccionario(palabras)

    frase = input("Introduce frase a traducir: ")
    print(traducirFrase(frase, diccionario))



if __name__ == "__main__":
    main()