import random
import functools
import os
import sys

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def game():
    #Funcion para reiniciar el juego al terminar
    def replay():
        select = input('¿Quieres jugar nuevamente (Selecciona [Y/n])?: ').upper()
        if select == 'Y':
            clear()
            game()
        elif select == 'N':
            return sys.exit()
        else:
            clear()
            print('Porfavor selecciona una opcion valida')
            replay()

    words = ['CASA', 'PERRO', 'GATO', 'PYTHON']
    letter_list = []
    lifes = 5

    game_word = random.choice(words)
    clear()
    #Solo para pruebas
    #print(game_word)
    game_var = list('_'*len(game_word))
    print('*'*7, 'JUEGO DEL AHORCADO', '*'*7)

    while lifes != 0:
        show_var = functools.reduce(lambda counter, item: counter+item, game_var)
        
        print('Descubre la palabra: ', show_var)
        print(f'Tienes {lifes} vidas') 
        
        if show_var != game_word:
            player_letter = input('Escoge una letra: ').upper()
            if player_letter in letter_list:
                player_letter
                lifes -= 1
                clear()
                print('Ya usaste esta letra')
                
            elif len(player_letter) > 1:
                clear()
                print('¡Cuidado, solo puedes ingresar una letra!')
                player_letter
            else: 
                letter_list.append(player_letter)
                if player_letter not in game_word: 
                    lifes -= 1
                    clear() 
                else:
                    for i in range(len(game_word)):
                        if list(game_word)[i] == player_letter:
                            game_var[i] = player_letter
                            clear()
            
            print('*'*7, 'JUEGO DEL AHORCADO', '*'*7)
            print(f'Has utilizado estas letras: {sorted(letter_list)}')   

        else:
            clear()
            print('*'*7, 'JUEGO DEL AHORCADO', '*'*7)
            print('*'*7, '¡FELICITACIONES HAS GANADO!', '*'*7)    
            replay()
    
    if lifes == 0:
        clear()
        print('*'*7, 'JUEGO DEL AHORCADO', '*'*7)
        print('*'*7, 'LO SENTIMOS HAS PERDIDO', '*'*7)
        replay()

if __name__ == '__main__':
    game()

    