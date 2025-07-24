def factor():
    print()
    print("Find factors of a number")
    print('---------------------------------------')

    def game():
        while True:
            try:
                num = int(input("Enter a number: "))
                print(f"Factors of {num} are: ", end="")
                for i in range(1, num+1):
                    if num % i == 0:
                        print(i, end=" ")
                print()
                print('---------------------------------------')
                break
            except ValueError:
                print("Enter a number")
    game()