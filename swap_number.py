def swap_number():
    
    print()
    print("Swap 2 numbers")
    print("_______________________________________")

    def game():
        while True:
            try:
                a = int(input("Enter 1st number (a): "))
                b = int(input("Enter 2nd number(b): "))
                a , b = b , a
                
                print(f"After swapping: a = {a}, b = {b}")
                print("_______________________________________")
                break
            except ValueError:
                print("Enter a valid number")

    game()