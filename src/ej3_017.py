"""
Ejercicio 3.2.4

Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""
    
def formatearFecha(fecha, meses):
    dia, mes, año = fecha.split("/")

    msg = str(dia) + " de " + str(meses["listameses"][int(mes)-1]) + " de " + str(año)

    return msg



def main():
    fecha = input("Introduce fecha en fromato (dd/mm/aaaa)")
    meses = {
        "listameses": ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]    
        }
    
    print(formatearFecha(fecha, meses))



if __name__ == "__main__":
    main()