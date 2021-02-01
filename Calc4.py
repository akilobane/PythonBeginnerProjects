#My calculator v4
import math

def basicOperations(x, y, selection):
    if selection == 1:
        return x + y
    elif selection== 2:
        return x - y
    elif selection == 3:
        return x * y
    elif selection == 4:
        return x / y

def values():
    num1 = float(input("Enter the first value: "))
    num2 = float(input("Enter the second value: "))
    return num1, num2

answer = input("Welcome to the beta v1.04 test for Akilobane's Calculator, would you like to test it?(Y/N)")
if answer in ['Yes', 'Y', 'y']:
    print('Welcome to my calculator!!!!')
    print('Here are the operations available: ')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Square Root')
    print('6.Exit')

    selection = int(input("Please make a selection (1,2,3,4,5,): "))

    if selection == 1:
        num1, num2 = values()
        print(f'{num1} + {num2} = {basicOperations(num1, num2, selection)}')
        exit()
    elif selection == 2:
        num1, num2 = values()
        print(f'{num1} - {num2} = {basicOperations(num1, num2, selection)}')
    elif selection == 3:
        num1, num2 = values()
        print(f'{num1} * {num2} = {basicOperations(num1, num2, selection)}')
    elif selection == 4:
        num1, num2 = values()
        print(f'{num1} / {num2} = {basicOperations(num1, num2, selection)}')

else:
    print("Goodbye. ")
