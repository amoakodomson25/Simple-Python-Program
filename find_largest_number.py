def find_largest():

    print()
    print("Find Largest number between 2 numbers")
    print('---------------------------------------')

    def game():
        while True:
            try:
                a = int(input("Enter 1st number (a): "))
                b = int(input("Enter 2nd number(b): "))

                if a > b:
                    print(f"{a} is larger than {b}")
                    print
                    break
                elif b > a:
                    print(f"{b} is larger than {a}")
                    print
                    break
                else:
                    print(f"{a} is equal to {b}")
                    print
                    break
            except ValueError:
                print("Enter a valid number")

    game()