"""
Ejercicio 3.2.4

Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""

def formatFecha(fecha, mes):
    

def main():
    fecha = input("Introduce fecha en fromato (dd/mm/aaaa)")
    dia, mes, año = fecha.split("/")
    
    fecha = {
        "dia": dia,
        "mes": ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"],
        "año": año    
        }
  

if __name__ == "__main__":
    main()