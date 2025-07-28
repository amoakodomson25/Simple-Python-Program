from find_largest_number import find_largest
from swap_number import swap_number
from find_if_odd_or_even import odd_or_even
from find_sqrt import calculate_sqrt
from multiplication_table import multi
from fibonaci import fib
from sort_num_asc import sort_asc
from sort_num_dsc import sort_dsc
from find_largest_number_multiple import find_largest_2
from find_smallest_number_multiple import find_smallest
from factor_of_no import factor
from factorial import factorial


def program_hub():
    while True:
        try:
            print()
            print("Simple Programs")
            print("_______________________________________")

            print("Select the program")
            print("[1] Swap 2 numbers")
            print("[2] Find the largest number between 2 numbers")
            print("[3] Check if number is odd or even")
            print("[4] Calculate Sqrt of a number")
            print("[5] Multiplication table")
            print("[6] Fibonacci Sequence up to n terms")
            print("[7] Sort numbers in ascending order")
            print("[8] Sort numbers in descending order")
            print("[9] Find the largest number between multiple numbers")
            print("[10] Find the smallest number between multiple numbers")
            print("[11] Find the factors of a number")
            print("[12] Find the factorial of a number")
            print("<99> To quit")
            print()
            select_program = int(input("What program do you want to run: "))
            print()

            if select_program == 1:
                swap_number()
            elif select_program == 2:
                find_largest()

            elif select_program == 3:
                odd_or_even()

            elif select_program == 4:
                calculate_sqrt()

            elif select_program == 5:
                multi()

            elif select_program == 6:
                fib()

            elif select_program == 7:
                sort_asc()

            elif select_program == 8:
                sort_dsc()
                        
            elif select_program == 9:
                find_largest_2()

            elif select_program == 10:
                find_smallest()

            elif select_program == 11:
                factor()
            
            elif select_program == 12:
                factorial()
                
            elif select_program == 99:
                break
        except ValueError:
            print("Type a number")

program_hub()
