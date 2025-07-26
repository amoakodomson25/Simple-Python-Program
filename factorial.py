def factorial():
    print()
    print("Find factors of a number")
    print('---------------------------------------')

    def check():
        while True:
            try:
                
                num = int(input("Enter a number: "))
                factorial=1
                for i in range(1, num +1):
                    factorial*=i
                print(f"The factorial of {num} is {factorial}")
                
                print()
                print('---------------------------------------')
                break
            except ValueError:
                print("Enter a number")
    game()
