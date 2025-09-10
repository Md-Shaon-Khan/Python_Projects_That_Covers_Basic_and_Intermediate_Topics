import math

def show_menu():
    print("\n----------Simple Calculator----------")
    print("1. Addition (+)")
    print("2. Substraction (-)")
    print("3. Multipication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. power (x^y)")
    print("7. Square Root (√x)")
    print("8. Exit")

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input!")

def add(a , b):
    return a + b

def substract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    if b == 0:
        return "Error! Division by Zero."
    return a / b

def modulus(a , b):
    return a % b

def power(a , b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error! Number must be greater or equal than Zero(0)."
    return math.sqrt(a)

def calculator():
    while True:
        show_menu()
        choice = int(input("Choose an operation (1-8): "))

        if choice == 8:
            print("Exiting...Thank you for using me.")
            break

        elif choice == 7:
            num = get_number("Enter a number: ")
            print("Result: ",round(square_root(num),2))

        else:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == 1:
                print("Sum is: ",num1," + ",num2," = ",add(num1,num2))
            elif choice == 2:
                print("Substraction is: ",num1," - ",num2," = ",substract(num1,num2))    
            elif choice == 3:
                print("Multiply is: ",num1," * ",num2," = ",multiply(num1,num2))
            elif choice == 4:
                print("Division is: ",num1," / ",num2," = ",divide(num1,num2))
            elif choice == 5:
                print("Modulus is: ",num1," % ",num2," = ",modulus(num1,num2))
            elif choice == 6:
                print("Power is: ",num1," ^ ",num2," = ",power(num1,num2))
            else:
                print("Invalid choice!")

calculator()