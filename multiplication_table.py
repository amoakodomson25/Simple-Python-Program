def multi():
    print()
    print("Get multiplication table of a number")
    print("_______________________________________")

    def print_table():
        while True:
            try:
                num = int(input("Enter the number: "))
                for i in range(1,13):
                    print(f"{num} * {i} = {num*i}")
                print("_______________________________________")
                break
            except ValueError:
                print("Enter a valid number")
    print_table()

