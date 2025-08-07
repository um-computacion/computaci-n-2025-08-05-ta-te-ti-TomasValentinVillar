from tateti import Tateti
from tablero import Ganador, Empate


def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    while True:
        print("Tablero: ")
        for i in juego.tablero.contenedor:
            print(i)
        print("Turno: ")
        print(juego.turno)
        try:
            fil = int(input("Ingrese fila: "))
            col = int(input("Ingrese col: "))
            juego.ocupar_una_de_las_casillas(fil, col)
        
        except Ganador as e:
            for i in juego.tablero.contenedor:
                print(i)
            print(e)
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