import math

def calculate_sqrt():
    print()
    print("Calculate Squareroot of a number")
    print('---------------------------------')

    def calculateSqrt():
        while True:
            try:
                num = float(input("Type a number"))
                result = math.sqrt(num)
                print(f"The Square Root of {num} is {result}")
                break
            except ValueError:
                print("Enter a number")
    calculateSqrt()
