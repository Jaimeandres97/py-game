import random
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def choose_options():
    computer_option = ("piedra", "papel", "tijera")
    computer = random.choice(computer_option)
    computer_choice = computer.lower()
    user_option = input("Escoge porfavor ¿Piedra, papel o tijera?: ").lower()
    if user_option in computer_option:
        return user_option, computer_choice
    else:
        print('¡CUIDADO! No es una opcion válida')
        choose_options()
        return user_option, computer_choice


def game_rules(user_option, computer_choice, victory, defeat, round):
    if user_option == computer_choice:
        print(f"Empate, tu rival seleccionó {computer_choice} y tu escogiste {user_option}")
    elif (user_option == "piedra" and computer_choice == "tijera") or (user_option == "papel" and computer_choice == "piedra") or (user_option == "tijera" and computer_choice == "papel"):
        print(f"Ganaste! tu rival seleccionó {computer_choice} y tu escogiste {user_option}")
        victory += 1
    else:
        print(f"Perdiste, tu rival seleccionó {computer_choice} y tu escogiste {user_option}")
        defeat += 1
    print("Tu puntaje es: ", victory)
    print("El puntaje de tu rival es: ", defeat)
    round += 1
    return victory, defeat, round

def check_winner(victory, defeat):
    if victory == 2:
        print("Felicitaciones has ganado!")
    elif defeat == 2:
        print("Has sido derrotado por un robot")

def run_game():
    victory = 0
    defeat = 0
    round = 1
    
    while victory < 2 and defeat < 2:
        
        print("*" * 15)
        print("ROUND", round)
        print("*" * 15)
        
        user_option, computer_choice = choose_options()
        clear()
        victory, defeat, round = game_rules(user_option, computer_choice, victory, defeat, round)
    
    check_winner(victory, defeat)
    

if __name__ == '__main__':
    run_game()

