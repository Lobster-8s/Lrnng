
list1 = [1, 2, 4, 8, 16, 32]

def simple_multiplication(local_list):

    print(f"The Subject is {local_list}\n")
    N_One = 1
    N_Zero = 0
    for _ in local_list:
        try:
            test = (
                    local_list[ len(local_list) - ( len(local_list) - N_One )]
                    /
                    local_list[ len(local_list) - ( len(local_list) - N_Zero )]
                    )

            if test.is_integer():
                print(f"{local_list[ len(local_list) - ( len(local_list) - N_One )]} Divided by {local_list[ len(local_list) - ( len(local_list) - N_Zero )]} Equals {test}")

            else:
                print(f"{local_list[ len(local_list) - ( len(local_list) - N_One )]} Divided by {local_list[ len(local_list) - ( len(local_list) - N_Zero )]} Equals {test}")
                print("The Rule is Not a Simple Multiplication")
                return False

        except IndexError:
            print("\n---All elements have been tested---")

        N_One += 1
        N_Zero += 1

    print(f"The Rule is:\n  Next = Previous * {test}")
    return True


simple_multiplication(list1)
