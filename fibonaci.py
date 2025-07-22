def fib():
    print()
    print("Fibonacci Sequence up to n terms")
    print("_______________________________________")

    def game():
        while True:
            try:
                num = int(input("Enter the number of terms: "))
                a, b = 0, 1
                for _ in range(num):
                    print(a)
                    a, b = b, a + b

                print("_______________________________________")   
                break
            except ValueError:
                print("Enter a valid number")    
    game()
