def find_largest_2():

    print()
    print("Find Largest number in an array")
    print("_______________________________________")

    def game():
        while True:
            try:
                numbers = list(map(int, input("Enter numbers separated by space: ").split()))
                print(f"The largest number is {max(numbers)}")
                break
            except ValueError:
                print("Enter a valid number")

    game()