def odd_or_even():
    print()
    print("Is a number odd or even")
    print('---------------------------------------')

    def find():
        while True:
            try:

                num = int(input("Type a number: "))

                if (num % 2 == 1):
                    print(f"{num} is an odd number")                                        
                    print("_______________________________________")
                    break
                else:
                    print(f"{num} is an even number")                                
                    print("_______________________________________")

                    break   

            except ValueError:
                print("Enter a number")
    find()

