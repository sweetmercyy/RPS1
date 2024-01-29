import random
def rps ():
    pcredits = 0
    print(f"You currently have {pcredits} credits.")
    while True:
        user_action = input("Pick your action. ('rock', 'paper', or 'scissors'): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
   
        if user_action == computer_action:
            print(f"Both players chose {user_action}. It's a tie!")
            print(f"You now have {pcredits} credits.")
        if user_action == "rock":
            if computer_action == "paper":
                print(f"You chose {user_action}, Opponent chose {computer_action}. You lose!")
                pcredits = pcredits - 1
                print(f"You now have {pcredits} credits.")
            elif computer_action == "scissors":
                print(f"You chose {user_action}, Opponent chose {computer_action}. You win!")
                pcredits = pcredits + 1
                print(f"You now have {pcredits} credits.")
        if user_action == "scissors":
            if computer_action == "rock":
                print(f"You chose {user_action}, Opponent chose {computer_action}. You lose!")
                pcredits = pcredits - 1
                print(f"You now have {pcredits} credits.")
            elif computer_action == "paper":
                print(f"You chose {user_action}, Opponent chose {computer_action}. You win!")
                pcredits = pcredits + 1
                print(f"You now have {pcredits} credits.")
        if user_action == "paper":
            if computer_action == "scissors":
                print(f"You chose {user_action}, Opponent chose {computer_action}. You lose!")
                pcredits = pcredits - 1
                print(f"You now have {pcredits} credits.")
            elif computer_action == "rock":
                print(f"You chose {user_action}, Opponent chose {computer_action}. You win!")
                pcredits = pcredits + 1
                print(f"You now have {pcredits} credits.")