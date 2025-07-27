def sort_dsc():
    print()
    print("Sort numbers in descending order")
    print("_______________________________________")


    def sort():
            while True:
                try:
                    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
                    numbers.sort(reverse=True)
                    print("Sorted list: ", numbers)
                    print("_______________________________________")   
                    break
                except ValueError:
                    print("Enter a valid number")    
    sort()
