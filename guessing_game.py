## The Challenge:

#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

# - If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# - On a player's first turn, if their guess is
#       within 10 of the number, return "WARM!"
#       further than 10 away from the number, return "COLD!"
# - On all subsequent turns, if a guess is
#       closer to the number than the previous guess return "WARMER!"
#       farther from the number than the previous guess, return "COLDER!"
# - When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

# ---------------------------------------------------------------------------------------------------------------------------

import random

num = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

#Create a list to store guesses:
guesses = [0]

#Creating a while loop that asks for a valid guess:
while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    
    # here we compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
        
    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    
    # if we append all new guesses to the list, then the previous guess is given as guesses[-2]
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section.
    # We write "if guesses[-2]" -> this checks whether there is a value at guesses[-2]. If there isn't
    # this means this is the first guess, and the code at the else section executes:
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')