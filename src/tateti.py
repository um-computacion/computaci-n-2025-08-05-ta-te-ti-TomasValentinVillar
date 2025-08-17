from src.tablero import Tablero
from src.jugador import Jugador
from src.excepciones import FueraDeRango,NombreVacio

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.jugadores = {}

    def crear_jugador(self,nom,ficha,estado):
        if nom == "":
            raise NombreVacio("No se puede ingresar nombre vacío")
        jugador = Jugador(nom,ficha,estado)
        self.jugadores[ficha] = jugador
    def verificar_rango(self,fil, col):
        if fil < 0 or fil > 2:
            raise FueraDeRango("Fila fuera de rango")
        if col < 0 or col > 2:
            raise FueraDeRango("Columna fuera de rango")
    def ocupar_una_de_las_casillas(self, fil, col):
        self.verificar_rango(fil,col)
        self.tablero.poner_la_ficha(fil, col, self.turno)
        self.tablero.verificar_ganador()
        self.tablero.verificar_empate()
        if self.turno == "X":
            self.turno = "0"
        else:
            self.turno = "X"
    def definir_ganador(self):
        if self.turno == 'X':
            perdedor = '0'
        else:
            perdedor = 'X'
        self.jugadores[self.turno].estado = 'Ganador'
        self.jugadores[perdedor].estado = 'Perdedor'
    def definir_empate(self):

        self.jugadores['X'].estado = 'Empate'
        self.jugadores['0'].estado = 'Empate'