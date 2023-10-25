import math
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




    elif (selection == 9):
        result = 0
        print(result)
        result = float(input("Select a number: "))

    elif (selection == 10):
        print("GoodBye!")
        break

