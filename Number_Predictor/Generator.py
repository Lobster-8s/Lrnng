import random

def generate(length):

    Casual_Decision = random.randint(0, 100)
    multiplier =  random.randint(1,10)
    adder = random.randint(-100,100)
    starter = random.randint(1, 2)

    local_sequence = [starter]
    if Casual_Decision <= 50:
        for i in range(length):
         local_sequence.append(local_sequence[-1] * multiplier + adder)

        if adder > 0:
            local_rule = f"Next = Previous * {multiplier} + {adder}"
        else:
            local_rule = f"Next = Previous * {multiplier} {adder}"
        return local_sequence, local_rule

    elif Casual_Decision <= 65:
        for i in range(length):
            local_sequence.append(local_sequence[-1] * multiplier)
        local_rule = f"Next = Previous * {multiplier}"
        return local_sequence, local_rule

    elif Casual_Decision <= 80:
        for i in range(length):
            local_sequence.append(local_sequence[-1] + adder)
        local_rule = f"Next = Previous + {adder}"
        return local_sequence, local_rule

    elif Casual_Decision <= 100 and starter == 1: #Basically Fibonacci....
        local_sequence.append(starter)
        for i in range(length):
            local_sequence.append(local_sequence[-1] + local_sequence[-2])
        local_rule = f"Fibonacci Sequence"
        return local_sequence, local_rule
    return "Brother something's REALLY Wrong", None


def main():
    while True:
        print("Press Enter to generate a sequence and a rule.\nType 'Q' and enter to quit.")
        if input() == "Q":
            break
        else:
            sequence, rule = generate(int(input("How many numbers do you want your sequence to have?\n>>")))
            print("--------------------------------\n----------NEW SEQUENCE----------\n--------------------------------")
            print(f"Sequence: {sequence}")
            print(f"Rule: {rule}\n")

main()