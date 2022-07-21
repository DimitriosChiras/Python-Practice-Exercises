# We will mimic the cups and ball with a Python list (2 empty strings and one wit a capital O for the ball).#
# It will also not show the shuffle to the user, making the user's guess completely random (ie can't follow it with their eyes).

from random import shuffle

# First we create a function that shuffles mylist
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# Then we create a function to take user's guess:
def player_guess():
    guess=''
    while guess not in ['0','1','2']:  
        guess = input("Pick a number! 0, 1 or 2")
    return int(guess)

# For above: we are starting with an empty placeholder for the player's guess. 
# We are then adding a while loop for the cases where the player had not put 0,1 or 3, to keep asking to pick a number.
# Input always returns a STRING so we are checking for strings of 0,1,2
# Once the input is in and it is 0, 1 or 2, return the integer version of it

# Now we need one more function that will combine the list that has been shuffled, with the player's guess,
# to check whether the guess has been correct or not.
def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(f"Here's where the ball was! {mylist}")

# Logic:

#INITIAL LIST
mylist=[' ','O',' ']

#SHUFFLE LIST
mixedup_list=shuffle_list(mylist)

#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixedup_list,guess)