def find_smallest():

    print()
    print("Find smallest number in an array")
    print("_______________________________________")

    def find():
        while True:
            try:
                numbers = list(map(int, input("Enter numbers separated by space: ").split()))
                print(f"The smallest number is {min(numbers)}")
                break
            except ValueError:
                print("Enter a valid number")

    find()
