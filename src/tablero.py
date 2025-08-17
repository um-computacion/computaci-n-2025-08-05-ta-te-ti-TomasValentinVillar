from src.excepciones import Ganador,PosOcupadaException, Empate, FueraDeRango

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        # ver si esta ocupado...
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("pos ocupada!")
    
    def verificar_ganador(self):
        #verifica fila
        for i in self.contenedor:
            j = i[0]
            if j == i[1] and j == i[2] and j != "":
                raise Ganador("Ganaste!")
            
        #verifica columna
        contador = 0
        for i in self.contenedor[0]:
            if i == self.contenedor[1][contador] and i == self.contenedor[2][contador] and i != "":
                raise Ganador("Ganaste!")
            contador = contador + 1
        #verificar diagonal
        x = self.contenedor[0][0]
        y = self.contenedor[1][1]
        z = self.contenedor[2][2]        
        for i in range(0,2):
            if x == y == z != "":
                raise Ganador("Ganaste!")
            x = self.contenedor[0][2]
            z = self.contenedor[2][0]
    def verificar_empate(self):
        contador = 0
        for i in self.contenedor:
            for j in i:
                if j != "":
                    contador = contador + 1
        if contador == 9:
            raise Empate("Empate!")
    def verificar_rango(self,fil, col):
        if fil < 0 or fil > 2:
            raise FueraDeRango("Fila fuera de rango")
        if col < 0 or col > 2:
            raise FueraDeRango("Columna fuera de rango")
        

            

