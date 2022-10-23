def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Simple Anime Quiz ")
print("")
guess1 = input("1.Haikyu!! is an anime centred around a boy who wants to be successful in which sport?")
check_guess(guess1, "Volleyball")
guess2 = input("2.In the first season of In Sword Art Online, what is the black blade used by Kirito called? ")
check_guess(guess2, "The Elucidator")
guess3 = input("3.As of 2021, what is the highest-grossing anime movies of all time?")
check_guess(guess3, "Demon Slayer: Mugen Train")
print("Your Score is "+ str(score))
