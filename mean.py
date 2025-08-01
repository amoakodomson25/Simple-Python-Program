def mean():
    print()
    print("finding mean")
    print("_______________________________________")


    def find_mean():
            while True:
                try:
                    frequncies = list(map(float, input("Enter frequencies of categories: ").split()))
                    sum_frequncies = sum(frequncies)
                    mean = sum_frequncies/len(frequncies)

                    print(mean)
                    break
                except ValueError:
                    print("Enter a valid number")    
    find_mean()

