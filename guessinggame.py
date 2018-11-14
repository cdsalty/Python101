#Import any modules needed
import random

# Ask the user for his or her name...
userName = raw_input("What is your name? ")

# Set up the (not-so) secret number as 5.
#secret_number = 5
secret_number = random.randint(1, 10)
# Init the bool gameOn to True
gameOn = True
#Number of allowed guesses
allowedGuesses = 5
# Init keepPlaying to True for the first game.
keepPlaying = True

#Initialize userGuesses
userGuesses = 0
while (keepPlaying): 
# Run a loop until gameOn = False
    while(gameOn):
        # get the users Input and store it in userGuess (we imported the module at the veryt beginning.)
        userGuess = raw_input("Guess a number between 1 and 10 ")
        userGuessAsInt = int(userGuess)
        # if the userGuess = the secret number, then... 
        # change goneOn = False
        # single = means assignment, == compare
        # the user made a guess, count it
        userGuesses += 1
    #Now, it is time to check the user's guess
        if(userGuessAsInt == secret_number):
            # the user guessed the right number (or we wouldnt Run
            # this code) so change gameOn to false, so we can
            # quit the loop
            gameOn = False
            # Congratulate the user for being awesome!!
            print "Great job, %s. Game over." % userName
        # If the user did not guess teh right number, tell them
        # to guess again
        else:
            if(userGuesses == allowedGuesses):
                gameOn = False
                print "You are out of guesses! The nuymber was %i" % secret_number
                
            # Else if being used; else-if the user is too high, tell them
            elif(userGuessAsInt > secret_number):
                # print "Your guess is too high"
                print "%i is too high" % userGuessAsInt
                #HERE, we take allowedGuesses and subtract userGuesesses from it; the formula is listed outside of %;
                print "you have %i guesses left" % (allowedGuesses - userGuesses)
            # if the user guess isn't too high, and it's not right
            # then it must be... to low
            else:
                # print "Your guess is too low"
                # option 1. print userGuess + " is too low"            
                # option 2. print str(userGuessAsInt) + " is too low"            
                # Interpolation = mixing strings and variables
                # In Python, you can interpolate with a % sign
                print "%s, %i is too low" % (userName,userGuessAsInt)

                print "Guess again..."
                print "you have %i guesses left" % (allowedGuesses - userGuesses)
    playAgain = raw_input("Would you like to play again (y or n)")
    if (playAgain == "n"):
        keepPlaying = False
        print "Thanks for playing, %s" % userName
    else:
        #reset our variables and get a new number
        secret_number = random.randint(1, 10)
        #reset gameOn
        gameOn = True 
        # reset their number of guesses
        userGuesses = 0
