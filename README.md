## Ejecución de interfáz

```text
python -m src.cli
```

## Ejecución de los tests

```text
python -m unittest
```

## Nombre y Breve descrippción del código

Nombre y Apellido: Tomas Villar

El código está divido en src y test, en la carpeta src se encuentran las clases Tateti, Jugador, Tablero y CLI, cada una en su respectivo archivo y un archivo para las excepciones. La clase Tateti se encarga de ocupar las casillas en el tablero, crear a los dos jugadores, definir el estado de los juadores de Ganador, Perdedor o Empate y también verifica el rango del indice para ocupar una casilla en el tablero. La clase Tablero es la que verifica si se pueden poner o no fichas en el tablero según las fichas que esté, en cada casilla, también sabiendo las fichas de cada casilla verifica si ganó y perdió cada jugador y en el caso que se llenen todas las casillas defiene el empate, es decir que tablero es la clase que con la información de las fichas de las casillas toma las deciciones. La clase Jugador guardará el nombre del jugador, su ficha y el estado, que este puede ser Jugando, Ganador, Perdedor y Empate. Cli es la interfaz que interacturá con el usuario y llama a las funciones de Tateti.

Las funciones son testadas en tests de la carpeta test


