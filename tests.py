import unittest
from tablero import Tablero,Ganador,Empate
from tateti import Tateti

class TestTaTeTi(unittest.TestCase):
    
    def test_ganar_filas1(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["X", "", ""],
            ["X", "", ""],
            ["X", "", ""],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()
    def test_ganar_filas2(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["", "0", ""],
            ["", "0", ""],
            ["", "0", ""],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()

    def test_ganar_filas3(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["", "", "X"],
            ["", "", "X"],
            ["", "", "X"],
        ]
        with self.assertRaises(Ganador):
            juego.tablero.verificar_ganador()