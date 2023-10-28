import math

TRIG_FUNCS = [math.sin, math.cos, math.tan, math.asin, math.acos, math.atan]

result = float(input("Select a number: "))

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

def GetNumber(input, _type):
    success =1
    value =0
    try:
        value =_type(input)
    except ValueError:
        success =0
        print("Invalid Input. Please re-enter input.")
    return value, success

def DoTrigFunction(choice):
    success =0
    value =0

    if choice>=1 and choice <=6:
        value, success = GetNumber(input("Please enter value."), float)
        if not success:
            return value, success
        else:
            if value >= 4 and value <=6 and (value <-1 or value >1):
                print("Invalid Input. Please re-enter input.")
            else:
                # Input should be fine here ..
                value =TRIG_FUNCS[choice](value)
                return value, success
    else:
        print("Invalid Input. Please re-enter input.")
        return value, success

def DoTrignometry():
    value, success = GetNumber(input("Please enter your choice: "), int)
    if not success:
        return value, success
    else:
        choice =value
        while True:
            value, success =DoTrigFunction(choice)
            if success:
                # Finish execution ..
                return value, success
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
    mainMenu()
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
        while True:
            result, success = DoTrignometry()
            if success:
                print(result)
                break
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
