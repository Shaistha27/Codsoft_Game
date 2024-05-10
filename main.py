import random
import os


def selectRock():
    global user_score, computer_score

    if computer_choice == rock:
        print(
            f'\nUser Choice : {user_choice}\nComputer Choice : {computer_choice}'
        )
        print(
            f"TIE\nUser Score : {user_score}\nComputer Score : {computer_score}"
        )

    elif computer_choice == paper:
        computer_score += 1
        print(
            f'\nUser Choice : {user_choice}\nComputer Choice : {computer_choice}'
        )
        print(
            f"YOU LOSE\nUser Score : {user_score}\nComputer Score : {computer_score}"
        )
    elif computer_choice == scissors:
        user_score += 1
        print(
            f'\nUser Choice : {user_choice}\nComputer Choice : {computer_choice}'
        )
        print(
            f"YOU WIN\nUser Score : {user_score}\nComputer Score : {computer_score}"
        )


def selectPaper():
    global user_score, computer_score
    if computer_choice == rock:
        user_score += 1
        print(
            f'\nUser Choice : {user_choice}\nComputer Choice : {computer_choice}'
        )
        print(
            f"YOU WIN\nUser Score : {user_score}\nComputer Score : {computer_score}"
        )

    elif computer_choice == paper:
        print(
            f'\nUser Choice : {user_choice}\nComputer Choice : {computer_choice}'
        )
        print(
            f"TIE\nUser Score : {user_score}\nComputer Score : {computer_score}"
        )

    elif computer_choice == scissors:
        computer_score += 1
        print(
            f'\nUser Choice : {user_choice}\nComputer Choice : {computer_choice}'
        )
        print(
            f"YOU LOSE\nUser Score : {user_score}\nComputer Score : {computer_score}"
        )


def selectScissor():
    global user_score, computer_score
    if computer_choice == rock:
        computer_score += 1
        print(
            f'\nUser Choice : {user_choice}\nComputer Choice : {computer_choice}'
        )
        print(
            f"YOU LOSE\nUser Score : {user_score}\nComputer Score : {computer_score}"
        )
    elif computer_choice == paper:
        user_score += 1
        print(
            f'\nUser Choice : {user_choice}\nComputer Choice : {computer_choice}'
        )
        print(
            f"YOU WIN\nUser Score : {user_score}\nComputer Score : {computer_score}"
        )
    elif computer_choice == scissors:
        print(
            f'\nUser Choice : {user_choice}\nComputer Choice : {computer_choice}'
        )
        print(
            f"TIE\nUser Score : {user_score}\nComputer Score : {computer_score}"
        )


computer_score = 0
user_score = 0

text = '''
  _______      ___      .___  ___.  _______ 
 /  _____|    /   \     |   \/   | |   ____|
|  |  __     /  ^  \    |  \  /  | |  |__   
|  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  |__| |  /  _____  \  |  |  |  | |  |____ 
 \______| /__/     \__\ |__|  |__| |_______|
 '''

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  

    Rock
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  

    Paper
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  

    Scissors
'''

thankyou = ''''
.___________. __    __       ___      .__   __.  __  ___ ____    ____  ______    __    __  
|           ||  |  |  |     /   \     |  \ |  | |  |/  / \   \  /   / /  __  \  |  |  |  | 
`---|  |----`|  |__|  |    /  ^  \    |   \|  | |  '  /   \   \/   / |  |  |  | |  |  |  | 
    |  |     |   __   |   /  /_\  \   |  . `  | |    <     \_    _/  |  |  |  | |  |  |  | 
    |  |     |  |  |  |  /  _____  \  |  |\   | |  .  \      |  |    |  `--'  | |  `--'  | 
    |__|     |__|  |__| /__/     \__\ |__| \__| |__|\__\     |__|     \______/   \______/  

'''


def game():

    global user_choice, computer_choice

    art_list = [rock, paper, scissors]
    computer_choice = random.choice(art_list)

    user_choice = input(
        "\nEnter your choice (1. Scissor, 2. Paper or 3. Rock) : ").lower()
    if user_choice == '1' or user_choice == 'scissor':
        user_choice = scissors
        selectScissor()
    elif user_choice == '2' or user_choice == 'paper':
        user_choice = paper
        selectPaper()
    elif user_choice == '3' or user_choice == 'rock':
        user_choice = rock
        selectRock()
    else:
        print('Invalid Choice!')


game_continue = True

while game_continue:
    print(f'''
  _______      ___      .___  ___.  _______ 
 /  _____|    /   \     |   \/   | |   ____|                        
|  |  __     /  ^  \    |  \  /  | |  |__                           1. Play
|  | |_ |   /  /_\  \   |  |\/|  | |   __|                          2. Reset
|  |__| |  /  _____  \  |  |  |  | |  |____                         3. Exit
 \______| /__/     \__\ |__|  |__| |_______|       
''')
    ask = input("\nEnter your choice : ").lower()
    if ask == '1' or ask == 'play':

        game()
    elif ask == '2' or ask == 'reset':
        user_score = 0
        computer_score = 0
        continue
    elif ask == '3' or ask == 'exit':
        game_continue = False
        print(thankyou)
    else:
        print("Invalid Option")
