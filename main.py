from find_largest_number import find_largest
from swap_number import swap_number

def Game_hub():
    print()
    print ("Simple Programs")
    print('----------------------------')

    print("Select the program")
    print("<1> Swap 2 numbers")
    print("<2> Find the largest number")
    print()

    while True:
        try:
            select_program = int(input('What program do you want to run: '))
            print()

            if select_program == 1:
                swap_number()
                Game_hub()
            elif select_program == 2:
                find_largest()
                Game_hub()
            elif select_program == 99:
                break
        except ValueError:
            print("Type a number")


Game_hub()


