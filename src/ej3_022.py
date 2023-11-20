"""
Ejercicio 3.2.9

Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""



def añadirFactura(diccionario:dict) -> dict:
    numFactura = int(input("Numero factura: "))
    coste = float(input("Coste factura: "))
    
    diccionario[numFactura] = coste

    return diccionario



def pagarFactura(diccionario:dict, diccionarioPagadas:dict):

    numFactura = int(input("Numero de factura a pagar: "))
    diccionarioPagadas[numFactura] = diccionario[numFactura]
    diccionario.pop(numFactura)

    # En este caso no seria necesario retornan estos valores, ya que los cambios realizados se ehecutan una vez llamada la funcion, sin necesidad de retornarlos
    return diccionario, diccionarioPagadas



def mostrarCobros(diccionario:dict, diccionarioPagadas:dict):
    
    totalPagado = sum(diccionarioPagadas.values())
    totalPorPagar = sum(diccionario.values())

    print(f"Total pagado {totalPagado}€. Por pagar {totalPorPagar}€.")




def mostrarDiccionario(diccionario:dict):
    print("\nNumero Factura -- Cantidad\n")
    for k,v in diccionario.items():
        print(f"{k}  --  {v}€")
    

def main():
    diccionario = {}
    diccionarioPagadas = {}
    ok = False

    while not ok:
        opc = int(input("Elije una opcion (1/Añadir factura, 2/Pagar factura existente, 3/Terminar): "))

        if opc == 1:
            añadirFactura(diccionario)
            mostrarDiccionario(diccionario)
            mostrarCobros(diccionario, diccionarioPagadas)
        elif opc == 2:
            pagarFactura(diccionario, diccionarioPagadas)
            mostrarDiccionario(diccionario)
            mostrarCobros(diccionario, diccionarioPagadas)
        else:
            ok = True
            mostrarDiccionario(diccionario)
            mostrarCobros(diccionario, diccionarioPagadas)



if __name__ == "__main__":
    main()