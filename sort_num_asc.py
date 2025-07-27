def sort_asc():
    print()
    print("Sort numbers in ascending order")
    print("_______________________________________")


    def sort():
            while True:
                try:
                    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
                    numbers.sort()
                    print("Sorted list: ", numbers)
                    print("_______________________________________")   
                    break
                except ValueError:
                    print("Enter a valid number")    
    sort()
