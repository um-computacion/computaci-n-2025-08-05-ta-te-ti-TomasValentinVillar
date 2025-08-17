from src.tateti import Tateti
from excepciones import Ganador, Empate, PosOcupadaException, FueraDeRango



def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    nombre1 = input('Ingrese el nombre del jugador de a ficha X: ')
    nombre2 = input('Ingrese el nombre del jugador de a ficha Y: ')
    juego.crear_jugador(nombre1,'X','Jugando')
    juego.crear_jugador(nombre2,'0','Juagando')
    while True:
        print("Tablero: ")
        for i in juego.tablero.contenedor:
            print(i)
        print(f"Turno: {juego.jugadores[juego.turno].nombre}, Ficha: {juego.turno}")
        try:
            fil = int(input("Ingrese fila (entre 0 y 2): "))
            col = int(input("Ingrese col (entre 0 y 2): "))
            juego.ocupar_una_de_las_casillas(fil, col)
        
        except Ganador as e:
            for i in juego.tablero.contenedor:
                print(i)
            juego.definir_ganador()
            print(f'{e}, jugador {juego.jugadores[juego.turno].nombre}')
            break
        except Empate as e:
            for i in juego.tablero.contenedor:
                print(i)
            print(e)
            break
        except Exception as e:
            for i in juego.tablero.contenedor:
                print(i)
            print(e)



if __name__ == '__main__':
    main()