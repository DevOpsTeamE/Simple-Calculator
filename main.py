import math
#result = float(input("Select a number: "))
def mainMenu():
    print("1. Addition");
    print("2. Subtraction");
    print("3. Multiplication");
    print("4. Division");
    print("5. Trigonometry");
    print("6. Exponents");
    print("7. Square Root");
    print("8. Percentage");
    print("9. Clear");
    print("10. Exit Calculator")

def trigoMenu():
    print("1. Sine");
    print("2. Cosine");
    print("3. Tangent");
    print("4. Inverse Sine");
    print("5. Inverse Cosine");
    print("6. Inverse Tangent");

def perform_exponents():
    print("\nPerfom Exponents: ")
    num = float(input("Enter a number: "))
    power = int(input("Enter the exponent number: "))

    result = num**power

    print(f"Result: {result:.2f}\n") 

def convert_to_percentage():

    # Get user input as a decimal number
    number = float(input("Enter a decimal number between 0 and 1: "))
            
    # Check if the input is in the valid range (0 to 1)
    if 0 <= number <= 1:
        # Convert the number to a percentage
        percentage = number * 100
                
        # Print the result
        print(f"{number} as a percentage is: {percentage:.2f}%")
        
    else:
        print("Please enter a number between 0 and 1.")

def perform_square_root():
    value = float(input("Enter a number to squart root: "))
    sqr_root_value = math.sqrt(value)
    print(f"Result: {sqr_root_value:.2f}\n") 


while True:
    mainMenu();
    selection = float(input("Input your choice: "))
    if (selection == 1):
        num = float(input("Input number to add: "))
        result = result + num
        print(result)
    elif (selection == 2):
        num = float(input("Input number to subtract: "))
        result = result - num
        print(result)
    elif (selection == 3):
        num = float(input("Input number to multiply with: "))
        result = result * num
        print(result)
    elif (selection == 4):
        num = float(input("Input number to divide by: "))
        result = result/num
        print(result)
    elif (selection == 5):
        trigoMenu()
        trigoSelection = int(input("Input your choice: "))
    elif (selection == 6):
        perform_exponents()
    elif (selection == 7):
        perform_square_root()
    elif (selection == 8):
        convert_to_percentage()

    elif (selection == 9):
        result = 0
        print(result)
        result = float(input("Select a number: "))

    elif (selection == 10):
        print("GoodBye!")
        break

