from librerias import *

# CREAMOS LA CLASE TABLERO
class TableroFlota():

    # Función de inicialización. Entradas: jugador, barcos (nº y tamaño) y dimensión del tablero.
    def __init__(self, jugador, barcos, dimension_tablero):
        self.jugador = jugador
        self.dimension = dimension_tablero
        self.barcos = barcos

