import random

#generate a random number
answer=random.randint(1, 101)

print("Lets play a game!")
print("There 10 guesses for easy mode and 5 guesses for hard mode.")
difficulty_level= input("What mode do you wanna play? Type 'Easy' for easy and 'Hard' for hard: ").lower()
guess= int(input("Guess a number between 1 to 100: "))


def correct_or_not(guess):
    if guess==answer:
        print("You guessed it correctly yay!")
    if guess>answer:
        print("Too high")
    else:
        print("Too low")



if difficulty_level=='easy':
    for i in range(9,0, -1):
        if guess == answer:
            print("You guessed it correctly yay!")
            break
        else:
            # if guess==answer:
            #     print("You guessed it correctly yay!")
            #     break
            # else:
            if i==9:
                correct_or_not(guess)
            print(f"You have {i} guesses left")
            new_guess = int(input("Guess again: "))
            if new_guess == answer:
                print("You guessed it correctly yay!")
                break
            else:
                correct_or_not(new_guess)
    # print("You did not guess the number!")
    # print(f"the number was {answer}")
            # print(f"You have {i} guesses left")

if difficulty_level=='hard':
    for i in range(4,0, -1):
        if guess == answer:
            print("You guessed it correctly yay!")
            break
        else:
            # if guess==answer:
            #     print("You guessed it correctly yay!")
            #     break
            # else:
            if i==4:
                correct_or_not(guess)
            print(f"You have {i} guesses left")
            new_guess = int(input("Guess again: "))
            if new_guess == answer:
                print("You guessed it correctly yay!")
                break
            else:
                correct_or_not(new_guess)
    # print("You did not guess the number!")
    # print(f"the number was {answer}")
            # print(f"You have {i} guesses left")



