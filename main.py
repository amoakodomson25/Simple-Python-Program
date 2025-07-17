from find_largest_number import find_largest
from swap_number import swap_number
from find_if_odd_or_even import odd_or_even
from find_sqrt import calculate_sqrt












def Game_hub():
    print()
    print ("Simple Programs")
    print('----------------------------')

    print("Select the program")
    print("<1> Swap 2 numbers")
    print("<2> Find the largest number")
    print("<3> Check if number is odd or even")
    print("<4> Calculate Sqrt of a number")
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
            elif select_program == 3:
                odd_or_even()
                Game_hub()
            elif select_program == 4:
                calculate_sqrt()
                Game_hub()    
            elif select_program == 99:
                break
        except ValueError:
            print("Type a number")


Game_hub()


