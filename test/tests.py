import unittest
from src.excepciones import Ganador,Empate,PosOcupadaException, FueraDeRango, NombreVacio
from src.tateti import Tateti


class TestTaTeTi(unittest.TestCase):

   
    def test_ocupar_casilla(self):
        juego = Tateti()

        resultado = [
            ["X", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

        juego.ocupar_una_de_las_casillas(0,0)
        
        self.assertEqual(juego.tablero.contenedor, resultado)

    def test_ganar_columna1(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["X", "", ""],
            ["X", "", ""],
            ["X", "", ""],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()
    def test_ganar_columna2(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["", "0", ""],
            ["", "0", ""],
            ["", "0", ""],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()

    def test_ganar_columna3(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["", "", "X"],
            ["", "", "X"],
            ["", "", "X"],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()
    def test_ganar_fila1(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["X", "X", "X"],
            ["", "", ""],
            ["", "", ""],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()

    def test_ganar_fila2(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["", "", ""],
            ["0", "0", "0"],
            ["", "", ""],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()

    def test_ganar_fila3(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["0", "0", "0"],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()
    
    def test_ganar_diagonal1(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["X", "", ""],
            ["", "X", ""],
            ["", "", "X"],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()
    
    def test_ganar_diagonal2(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["", "", "0"],
            ["", "0", ""],
            ["0", "", ""],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()
    def test_empate(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["X", "0", "X"],
            ["X", "X", "0"],
            ["0", "X", "0"],
        ]
        with self.assertRaises(Empate):
            juego.tablero.verificar_empate()
    
    
    def test_pos_ocupada2(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["X", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
        with self.assertRaises(PosOcupadaException):
            juego.tablero.poner_la_ficha(0,0,'0')
    
    def test_crear_jugador(self):
        juego = Tateti()
        juego.crear_jugador('Tomas', 'X', 'Jugando')
        self.assertEqual('Tomas', juego.jugadores['X'].nombre)
        self.assertEqual('X', juego.jugadores['X'].ficha)
    def test_crear_jugador_nombre_vacío(self):
        juego = Tateti()
        with self.assertRaises(NombreVacio):
            juego.crear_jugador('', 'X', 'Jugando')
    def test_jugador_gana_X(self):
        juego = Tateti()
        juego.crear_jugador('Tomas', 'X', 'Jugando')
        juego.crear_jugador('Valentin', '0', 'Jugando') #ya viene por defecto que el juego está en turno X
        juego.definir_ganador()
        self.assertEqual(juego.jugadores['X'].estado, 'Ganador')
        self.assertEqual(juego.jugadores['0'].estado, 'Perdedor')

    def test_jugador_gana_0(self):
        juego = Tateti()
        juego.crear_jugador('Tomas', 'X', 'Jugando')
        juego.crear_jugador('Valentin', '0', 'Jugando')
        juego.turno = '0'
        juego.definir_ganador()
        self.assertEqual(juego.jugadores['X'].estado, 'Perdedor')
        self.assertEqual(juego.jugadores['0'].estado, 'Ganador')
    def test_jugador_empata(self):
        juego = Tateti()
        juego.crear_jugador('Tomas', 'X', 'Jugando')
        juego.crear_jugador('Valentin', '0', 'Jugando')
        juego.turno = '0'
        juego.definir_empate()
        self.assertEqual(juego.jugadores['X'].estado, 'Empate')
        self.assertEqual(juego.jugadores['0'].estado, 'Empate')

    def test_verificar_rango(self):
        juego = Tateti()
        with self.assertRaises(FueraDeRango):
            juego.verificar_rango(-1,1)
        with self.assertRaises(FueraDeRango):
            juego.verificar_rango(3,1)
        with self.assertRaises(FueraDeRango):
            juego.verificar_rango(1,-1)
        with self.assertRaises(FueraDeRango):
            juego.verificar_rango(1,3)
    


