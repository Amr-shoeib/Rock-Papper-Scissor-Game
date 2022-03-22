from ast import If
from random import choices, randint
from secrets import choice

choices = ["rock", "paper", "scissor"]
#player_choice  = paper
player_lives = 1
computer_lives = 1
total_lives = 1

player_choice = False

def winorloss(status):
   # print("inside winorlose function; status is: ", status)
    print("You", status, "would you like to play again?")
    choice = input("Y ? N?")
    if choice == "N" or choice == "n":
        print("you chose to quit! Better luck next time!")
        exit()
    elif choice == "Y" or choice == "y":
         global player_lives
         global computer_lives
         global total_lives
         
         player_Lives == total_lives   
         computer_Lives == total_lives
    else:
        print("Make a valid choice Y or N")
        choice = input("Y / N? ")
                

while player_choice is False:
    print("==========*/ RPS GAME */=============")
    print("computer_lives:", computer_lives, "/", total_lives)
    print("player lives:", player_lives, "/", total_lives)
    print("=====================================")
    print("choose your weapon or type quit to exit")
    
    player_choice = choices[1]

    #print("index 1 in the choice array is" + player_choice)
    
    print("choose your weapon or type quit to exit\n")
    
    player_choice = input("choose rock, paper, or scissors: \n")
    if player_choice== "quit":
        print("you choose to quit")
        exit()
    print("user chose " + player_choice)

    # this will be AI choice -> random pick from the choices array

    computer_choice = choices[randint(0, 2)] 
    print("computer chose: " + computer_choice)

    if computer_choice==player_choice:
        print("tie")
    
    elif computer_choice == "rock":
        if player_choice == "scissors":
            print("you lose") 
            player_lives -= 1 
        else:
            print("you win")  
            computer_lives -= 1
            
    elif computer_choice == "paper":
        if player_choice == "scissors": 
            print("you win")  
            computer_lives -=1
        else:  
        
            print("you lose")  
            player_lives -=1
            
    elif computer_choice == "scissors":
        if player_choice == "paper": 
            print("you lose")  
            player_lives -= 1
        else:
            print("you win")
            computer_lives -= 1
    
        if player_lives == 0:
            winorloss("lose")
         
        if computer_lives == 0:
            winorloss("won")
           

    print("player lives:", player_lives)
    print("computer lives:", computer_lives)
    
    player_choice = False
    