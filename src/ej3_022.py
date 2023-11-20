"""
Ejercicio 3.2.9

Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""



def añadirFactura(diccionario:dict):
    numFactura = int(input("Numero factura: "))
    coste = int(input("Coste factura: "))
    






def main():
    diccionario = {}
    opc = int(input("Elije una opcion (1/Añadir factura, 2/Pagar factura existente, 3/Terminar): "))

    if opc == 1:
        añadirFactura(diccionario)







if __name__ == "__main__":
    main()