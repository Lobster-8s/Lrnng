"""
In this file I'll be trying to code a simple function to print out the Fibonacci numbers.

In fibonacci_sequence I created a list and appended to it "Number[-1] + Number[-2]", which means I appended the sum of the last and second to last values of this list.
With the function len() I got the length of the list "Number". (If we have the list Numbers(1, 2, 3, 5) then the len() of Numbers is 4, because it has four values.)

Also, we use print (*Numbers, sep=', ') to print out the list in a "Clean" way. The * simble prints out the list without spaces, brackets, nor commas, but with sep=', ' we tell it to separate each value in Numbers with a comma and a space.

For fibonacci_number instead of *Numbers, sep=', ' we print Numbers[-1] so it only prints the last number.
"""
import time

def fibonacci_sequence(User_Input):
    Numbers = [1, 1]
    while len(Numbers) <= User_Input - 1:
        Numbers.append(Numbers[-1] + Numbers[-2])
    print(*Numbers, sep=', ')

def fibonacci_number(User_Input):
    Numbers = [1, 1]
    while len(Numbers) <= User_Input:
        Numbers.append(Numbers[-1] + Numbers[-2])
    print(Numbers[-1])

def basically_operation_2_but_it_calculates_the_time_holy_damn_this_is_long(User_Input):
    Numbers = [1, 1]
    Start_Time = time.time()
    while len(Numbers) <= User_Input:
        Numbers.append(Numbers[-1] + Numbers[-2])
    End_Time = time.time()
    Elapsed_Time = End_Time - Start_Time
    print(f"{Numbers[-1]}\nIt took {Elapsed_Time:.6f} seconds to complete the operation")

def main(User_Choice):
    if User_Choice == 1:
        fibonacci_sequence(int(input("How many Fibonacci Numbers should be printed out?\n>>")))
    elif User_Choice == 2:
        fibonacci_number(int(input('What Fibonacci number do u want printed out?\nExample: ">> 100" will print the 100th number\n>>')))
    elif User_Choice == 3:
        basically_operation_2_but_it_calculates_the_time_holy_damn_this_is_long(int(input('What Fibonacci number do u want printed out?\nExample: ">> 100" will print the 100th number\n>>')))

if __name__ == "__main__":
    try:
        main(int(input("1 Fibonacci Sequence\n2 Print a Singular Fibonacci Number\n3 Basically Option number 2 but it calculates the time it takes to complete the operation\n>>")))
    except ValueError:
        print("Please... enter a Goddamn number next time")