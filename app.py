# Escribir un juego de piedra papel o tijera
# El usuario debe poder elegir una opción y la computadora debe elegir una opción al azar, también se le debe de advertir de una opción no válida.
# En cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de la elección de la computadora.
# El juego debe terminar cuando el jugador decida salir.
# Se debe mostrar el resultado final del juego.
# Se debe mostrar el número de rondas ganadas por el jugador y el número de rondas ganadas por la computadora.
# Se debe mostrar el número de empates.
# El minijuego debe controlar las entradas de usuario, colocarlas en minúsculas y verificar si son válidas.
# La piedra gana a las tijeras
# La tijera gana al papel
# El papel gana a la piedra

import random as rd

def game():
    rounds = 0
    player_wins = 0
    computer_wins = 0
    ties = 0
    options = ['piedra', 'papel', 'tijera']
    while True:
        player = input('Elige una opción (piedra, papel, tijera) o escribe "salir" para terminar el juego: ')
        if player == 'salir':
            break
        if player not in options:
            print('Opción no válida')
            continue
        computer = rd.choice(options)
        print(f'La computadora eligió: {computer}')
        if player == computer:
            print('Empate')
            ties += 1
        elif player == 'piedra' and computer == 'tijera':
            print('Ganaste')
            player_wins += 1
        elif player == 'tijera' and computer == 'papel':
            print('Ganaste')
            player_wins += 1
        elif player == 'papel' and computer == 'piedra':
            print('Ganaste')
            player_wins += 1
        else:
            print('Perdiste')
            computer_wins += 1
        rounds += 1
    print(f'Juegos jugados: {rounds}')
    print(f'Juegos ganados por el jugador: {player_wins}')
    print(f'Juegos ganados por la computadora: {computer_wins}')
    print(f'Empates: {ties}')

if __name__ == '__main__':
    game()

# Para ejecutar el programa, se debe de correr el siguiente comando en la terminal:
# python app.py
# El programa se ejecutará y se le pedirá al usuario que elija una opción, en este caso, piedra, papel o tijera.
# El usuario podrá elegir una opción o salir del juego.
# El programa le dirá al usuario si ganó, perdió o empató y le dirá cuántas veces ganó, perdió o empató.