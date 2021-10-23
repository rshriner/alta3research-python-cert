#!/usr/bin/env python3
"""rshriner | NTRS
   Python certification """

# import all required modules
import random
from os import system

# define main function
def main():
    # store message for user instruction
    message = """\
        The Magic PyBall!
        No question too silly - only silly answers!
        
        Type QUIT to exit
        
        """
    # initialize variables
    # create list of responses
    response = [
        "With certainty!",
        "Ground control to Major Tom...Check ignition and may God's love be with you.",
        "No... I'm afraid not.",
        "Maybe, I misunderstood you?",
        "Highly unlikely!",
        "Don't make me laugh!",
        "Outcome uncertain...",
        "Like a Donkey's butt in a pepper patch!",
        "Don't be crazy!",
        "You know it!",
        "Thanks for playing!  Goodbye!"]

    quest = ""
    # run the program until QUIT is received by user
    while quest != "QUIT":
        # clear screen before each user prompt, but display instruction message every time
        system('clear')
        print(message)
        # prompt for user response
        quest = input("What question do you have for the Magic PyBall?\n> ")
        # create a random index - subtract 2 to properly address lists and avoid goodbye message
        index = random.randint(0,len(response)-2)
        # store random response to ans
        ans = response[index]
        # print response and continue or quit
        print("\nMagic PyBall says...")
        if quest == "QUIT":
            # the last response is always the goodbye message
            ans = response[-1]
            print(f"{ans}\n")
            # break out of loop and end game
            break
        else:
            print(f"{ans}\n")
            # pause the screen for the user to read 
            input("Press ENTER to try again")

# only run main() when we are running from this program... this isn't really necessary unless we have additional functions in this script
if __name__ == "__main__":
    main()
