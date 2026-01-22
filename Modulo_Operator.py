"""
This file will be used to tinker around with the Modulo Operator %

The Modulo Operator returns the remainder of a division, so for 10 % 3 it would return 1 (10/3 = 3 , remainder of 1)

"""

def is_even(num):
    try:
        if int(num) % 2 == 0:
            print("Is Even")
        else:
            print("Is Not Even")
    except ValueError:
        print("Invalid Input")

def is_odd(num):
    try:
        if int(num) % 2 == 1:
            print("Is Odd")
        else:
            print("Is Not Odd")
    except ValueError:
        print("Invalid Input")

def cycle(num):
    try:
        for i in range(int(num)):
            print(i % 3)
    except ValueError:
        print("Invalid Input")

def example_for_shinobi(num):
    Shuriken_Textures = ["Texture1", "Texture2", "Texture3"]
    try:
        for i in range(int(num)):
            print(Shuriken_Textures[i % 3])
    except ValueError:
        print("Invalid Input")

def main():

    User_Input = input("\nChoose Operation:\n[1]Is_Even [2]Is_Odd [3]Cycle [4]Example4Shinobi\n>>")
    if  User_Input == "1":
        is_even(input("Choose A Number: "))
    elif User_Input == "2":
        is_odd(input("Choose A Number: "))
    elif User_Input == "3":
        cycle(input("Choose A Number: "))
    elif User_Input == "4":
        example_for_shinobi(input("Choose A Number: "))

if __name__ == "__main__":
    while True:
        main()