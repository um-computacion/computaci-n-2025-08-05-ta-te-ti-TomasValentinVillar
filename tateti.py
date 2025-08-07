from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.jugadores = {}

    def crear_jugador(self,nom,ficha,estado):
        jugador = Jugador(nom,ficha,estado)
        self.jugadores[ficha] = jugador
    def ocupar_una_de_las_casillas(self, fil, col):
        # pongo la ficha...
        self.tablero.poner_la_ficha(fil, col, self.turno)
        # condicion para ganar
        # cambia turno... va a suceder solo si se pudo poner la ficha
        self.tablero.verificar_ganador()
        #self.tablero.verificar_empate()
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