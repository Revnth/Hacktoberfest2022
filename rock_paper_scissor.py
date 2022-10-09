import random

user_points = 0
computer_points = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    # rock : 0 , paper : 1 , scissors : 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if(user_input == "rock" and computer_pick == "scissors"):
        print("You won!")
        user_points += 1
        continue
    elif(user_input == "paper" and computer_pick == "rock"):
        print("You won!")
        user_points += 1
        continue
    elif(user_input == "scissors" and computer_pick == "paper"):
        print("You won!")
        user_points += 1
        continue
    else:
        print("You lost!")
        computer_points += 1
        
print("You won",user_points,"times")
print("Computer won",computer_points,"times")

print("Goodbye!")    