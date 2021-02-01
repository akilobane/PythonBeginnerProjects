#My calculator version 3
import math

def addition(x, y):
    sum = x + y
    return sum

def subtract(x, y):
    sum = x - y
    return sum

def multiply(x, y):
    sum = x * y
    return sum

def divide(x, y):
     sum = x / y
     return sum

def square(x):
    sum = math.sqrt(x)
    return sum

answer = input("Welcome to the beta v1.02 test for Emil's Calculator, would you like to test it?(Y/N)")
if answer in ['Yes', 'Y']:
    print('Welcome to my calculator!!!!')
    print('Here are the operations available: ')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Square Root')
    print('6.Exit')

operation = input('Please make a selection (1,2,3,4,5,6): ')
if operation == '1':
            num1 = float(input('Please enter the first value: '))
            num2 = float(input('Please enter the second value: '))
            print(f'{num1} + {num2} = {addition(num1, num2)}')
elif operation == '2':
            num1 = float(input('Please enter the first value: '))
            num2 = float(input('Please enter the second value: '))
            print(f'{num1} - {num2} = {subtract(num1, num2)}')
elif operation == '3':
            num1 = float(input('Please enter the first value: '))
            num2 = float(input('Please enter the second value: '))
            print(f'{num1} * {num2} = {multiply(num1, num2)}')
elif operation == '4':
            num1 = float(input('Please enter the first value: '))
            num2 = float(input('Please enter the second value: '))
            print(f'{num1} / {num2} = {divide(num1, num2)}')
elif operation == '5':
            num = float(input('Please enter the number you want to square root: '))
            print(f'the square root of {num} is: {square(num)}')
elif operation == '6':
        print('You wasted my time... goodbye.')
else:
    print('Have a good day.')
