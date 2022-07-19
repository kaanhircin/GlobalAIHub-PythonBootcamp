import random

action_list = ['rock', 'paper', 'scissors']

player_score = 0
computer_score = 0

control = False

try:
    total_rounds = int(input("\nHow many rounds do you want to play? => "))
    control = True
    
    
    round_counter = 0

    while control == True:
    
        round_counter += 1
        print("\nRound number: ", round_counter)
        
        computer_choice = random.choice(action_list)
        player_choice = input("\nPlease choose your action: ")
        
        print("Computer: ", computer_choice)
        print("Player: ", player_choice)
        
        if computer_choice == player_choice:
            print("\nTie! Both players chose the same action.")

        elif computer_choice == 'paper':
            if player_choice == 'rock':
                print("Winner is computer.")
                computer_score += 1
            elif player_choice == 'scissors':
                print("Winner is player.")
                player_score += 1
        elif computer_choice == 'rock':
            if player_choice == 'paper':
                print("Winner is player.")
                player_score += 1
            elif player_choice == 'scissors':
                print("Winner is computer.")
                computer_score += 1
        elif computer_choice == 'scissors':
            if player_choice == 'rock':
                print("Winner is player.")
                player_score += 1
            elif player_choice == 'paper':
                print("Winner is computer.")
                computer_score += 1

        if round_counter == total_rounds:
            break

    if computer_score == player_score:
        print("\nThere is no winner, tie!", computer_score, ":", player_score)
    elif computer_score > player_score:
        print("\nComputer won with score", computer_score, ":", player_score)  
    elif computer_score < player_score:
        print("\nPlayer won with score", player_score, ":", computer_score)

except ValueError:
    print("You must enter a number!")
    control = False