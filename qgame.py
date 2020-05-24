from time import sleep

from gamelogic import Initialize_Quiz


def quotegame():
    print("QG: Welcome to the Quotes Game!! \nQG: I will show you a quote and you have to guess who said it! \nQG: But first, what is your name?")
    player_name = input()
    sleep(0.5)
    print(f"QG: Hello {player_name}, Welcome to QG")
    sleep(0.5)
    print("QG: You have 4 chances to guess who said the quote are you ready to play")
    sleep(0.5)
    response = input("QG: Type yes(y) or no(n): ").lower()
    sleep(1)
    count = 0
    ans, quote, bio, author_names = Initialize_Quiz()
    if response == "y" or response == "yes":
        print(f"\nQG: Who said this? \n{quote}")
        while(count < 5):
            sleep(0.5)
            # take user answer
            user_answer = input(f"{player_name} : ")
            # if answer is correct
            if user_answer == ans or user_answer in author_names:
                print(f"QG: You're right the author is {ans}!")
                sleep(0.5)
                # ask user if they want to continue
                print("QG: would you like to go again? ")
                go_again = input()
                # restart loop if user wants to continue
                if go_again == "y" or go_again == "yes":
                    ans, quote, bio, author_names = Initialize_Quiz()
                    print(f"QG: Who said this? \n\n{quote}")
                    count = 4
                    i = 0
                    continue
                else:
                    quit()
            elif(count < 4):
                # inform user they failed
                print(f"QG: Wrong answer try again")
                print(f"you have {4-count} chances ")
                print(bio[count])

            count += 1
        else:
            print(f"You lost its {ans}. Play again some other time! ")
            quit()

    else:
        quit()
