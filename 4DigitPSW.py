"""
I will be trying to create a program that asks the user for an unknown 4 digit Password in order to 'Access Secret Data'

I imported Random to create random Passwords, then I used Psw = f"{Psw:04d}" to make it so that the Password will
always have 4 digits. i.e.: If the Password is 14, it will become 0014.

Then I created the while True loop and read the user input, I used if User_Guess.isdigit() to check if the Guess was a Number,
if not I use elif UserGuess == "psw" to print out the randomly generated Password.
"""
import random

def main():

    Psw = random.randint(0, 9999)
    Psw = f"{Psw:04d}"

    while True:
        User_Guess = input("Enter the Password: ")

        if User_Guess.isdigit():
            User_Guess = f"{int(User_Guess):04d}"

            if User_Guess == Psw:
                print("Access To Secret Data: Granted")
                break
            else:
                print("Input: " + User_Guess)
                print("Access To Secret Data: Denied")

        elif User_Guess == "psw":
            print(Psw)
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()