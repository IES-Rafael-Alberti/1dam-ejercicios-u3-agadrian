"""
Ejercicio 3.3.1¶
Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:

[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]

Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que contenga cada domicilio una sola vez.
"""
# meto en un conjunto la ultima posicion de cada tupla de la lista

### OPERACIONES CONJUNTOS ###

## UNION (valores de a y b) -->  |
# a = {1,2,3}
# b = {3,4,5}
# union = a | b --> {1,2,3,4,5}

## INTERSECCION (valores que tienen ambos conjuntos) --> &
# a = {1,2,3}
# b = {3,4,5}
# intersccion = a & b --> {3}

## DIFERENCIA (valores de a que no estan en b) --> -
# a = {1,2,3}
# b = {3,4,5}
# diferencia = a - b  --> {1,2}

## INTERSECCION  SIMETRICA (valores de a y b, pero que no estan en ambos)
# a = {1,2,3}
# b = {3,4,5}
# interseccionSimetrica = a ^ b  --> {1,2,4,5}




def domiciliosClientes(lista:list):
    domicilios = set()
    for i in range(len(lista)):
        domicilios.add(lista[i][3])
    
    return domicilios


def main():
    lista = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]

    print(domiciliosClientes(lista))

if __name__ == "__main__":
    main()
