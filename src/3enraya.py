import os

# Simbolos tablero
FICHAS = (' ', 'X', 'O')


def borrarConsola():
    """ Limpiar consola """
    os.system("cls")



def pulsarTeclaContinuar():
    """
    Muestra mensaje Pulsa una tecla para continuar y hace una pausa hasta que se realice la accion
    """
    os.system("pause")



def crearFila(numColumnas = 3) -> list: # por defecto sera 3, si no le pasamos nada (no hace falta pasarle nada)

    return list(0 for _ in range(numColumnas)) # creo una tupla con 3 listas con 3 valores 0, que seria las columnas



def crearTablero(numFilas = 3) -> tuple: # por defecto sera 3, si no le pasamos nada (no hace falta pasarle nada)
    """
    Crear el tablero 3x3
    """

    return tuple(crearFila() for _ in range(numFilas))



def mostrarFila(fila: list):
    contenidoFila = "| "

    for celda in fila:
        contenidoFila += FICHAS[celda] + " | "

    print(contenidoFila)



def mostrarTablero(tablero: tuple):

    borrarConsola()
    print("-" * 13)
    for fila in tablero:
        mostrarFila(fila)
        print("-" * 13)



def cambiarTurno(turno: int) -> int:
    """
    Cambia el turno cada vez, siendo 1 o 2
    """

    if turno % 2 == 0:
        return 1
    return 2



def pedirPosicion(filaColumna: str, msj: str = "") -> int:

    posicion = None
    if msj != "": 
        print(msj)

    while posicion == None:
        try:
            posicion = int(input(f"Elije la {filaColumna} (1,2,3): ")) - 1 # visualemnte es del 1 al 3, no del 0 al 2
            if not 0 <= posicion <= 2:
                raise ValueError
        except ValueError:
            posicion = None
            print(f"** ERROR ** {filaColumna} no valida")
    return posicion



def comprobarCasilla(tablero: tuple, posicionFicha: dict) -> bool:

    return tablero[posicionFicha["fila"]][posicionFicha]



def colocarFicha(tablero: tuple, jugador: int):

    posicionFicha = {"fila": None, "columna": None}
    posicionCorrecta = False

    while not posicionCorrecta:
        posicionFicha["fila"] = pedirPosicion("fila", f"\nJugador {jugador}, coloque una ficha...")
        posicionFicha["columna"] = pedirPosicion("columna")

        posicionCorrecta = comprobarCasilla(tablero, posicionFicha)

        if posicionCorrecta:
            tablero[posicionFicha["fila"]][posicionFicha["columna"]] = jugador
        else:
            posicionFicha["fila"] = posicionFicha["columna"] = None
            print("** ERROR ** movimineto invalido")
            pulsarTeclaContinuar()
            mostrarTablero(tablero)



def verificarGanador(tablero) -> tuple:




def jugar(tablero: tuple):

    turno = 0
    ronda = 0
    hayGanador = False

    while not hayGanador:

        turno = cambiarTurno(turno)
        if turno == 1:
            ronda += 1

        print(f"\nRONDA {ronda}")
        print("-" * len(f"RONDA {ronda}") + "\n")

        #print(len(f"RONDA {ronda}"))

        colocarFicha(tablero, turno)
        mostrarTablero()

        if ronda >= 3:
            ganador, hayGanador = verificarGanador(tablero)
        
        if hayGanador:
            print(f"\nEl jugador {ganador} ha ganado\n")

        if ronda == 9:
            hayGanador = True
            print("\nEmpate!\n")



#
def main():
    
    tablero = crearTablero()
    mostrarTablero(tablero)
    jugar(tablero)

if __name__ == "__main__":
    main()