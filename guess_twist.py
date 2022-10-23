import random

pts=100
print("you have 100 initial points")
n=int(input("enter the number of tries you think you could guess in:\n "))
guess=0

while pts>0 or input()=="stop":
 
    if guess>n:
      print("you have crossed your boundaries")
      print(f"the number was {number}")
      break
 

    number = random.randint(1,20)
    user = int(input("Guess the number from range 1-20\n"))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        if n<=30: 
            if guess<=n/2:
              pts=pts+100
              print(f"your points are {pts}")
            else:
              pts=pts+30
              print(f"your points are {pts}")
        else:    
            pts=pts+10
            print(f"your points are {pts}")
        break
    elif user != number:
        print(f"Your guess is incorrect the number is {number}")
        pts=pts-20
        print(f"your points are {pts}")
    guess=guess+1
   
