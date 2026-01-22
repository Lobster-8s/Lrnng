"""
I will be trying to create a program that'll ask the user if he wants to use a random_brute_force_attack
or a sequential_brute_force_attack.

The sequential_brute_force_attack will instead start from guess 0000 and add 1 to it until it reaches the correct Password.

The random_brute_force_attack will generate a new guess after each attempt and will store the previous guesses
in Used_Guesses[], it will then compare the new guess with the contents of Used_Guesses[] to not repeat itself.
"""
import random

Psw = random.randint(0,9999)

def sequential_brute_force_attack():

    BF_Guess = 0

    for guesses in range(0, 9999):
        if BF_Guess == Psw:
            break
        else:
            print(BF_Guess)
        BF_Guess += 1

    print("The Password was: ", BF_Guess)
    main()

def random_brute_force_attack():

    Used_Guesses = []
    BF_Guess = random.randint(0,9999)

    while BF_Guess != Psw:
        if BF_Guess not in Used_Guesses:
            Used_Guesses.append(BF_Guess)
            BF_Guess = random.randint(0,9999)
            print(BF_Guess, " Was Not the Password")
            continue
        else:
            BF_Guess = random.randint(0,9999)
            print(BF_Guess, " Has already been used")
            continue

    print("The Password was: ", BF_Guess)
    print("Attempts: ", len(Used_Guesses))
    main()

def main():

    while True:
        User_Input = input("Select Type of Brute Force Attack: [s] sequential [r] random \n")
        if  User_Input == "s":
            sequential_brute_force_attack()
        elif User_Input == "quit":
            break
        else:
            random_brute_force_attack()


if __name__ == "__main__":
    main()