#Function to add the two numbers
def addition(num1, num2):
    return num1 + num2

#Function to subtract the two numbers
def subtraction(num1, num2):
    return num1 - num2

#Function to multiply the two numbers
def multiplication(num1, num2):
    return num1 * num2

#Function to divide the two numbers
def division(num1, num2):
    return num1 / num2

if __name__ == "__main__":
    #Give the user the options to choose from the menu
    print("Select operation.\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    #Take input from the user
    choice = input("Select operation number (1/2/3/4): ")

    #Take input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", addition(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtraction(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiplication(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", division(num1, num2))
    else:
        print("Invalid input")

