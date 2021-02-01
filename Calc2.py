#My Second Calculator Program
#This calculator uses functions, functions are used to break a program to smaller chunks. 'def' is the syntax for a function.
def addition(x, y):
    sum = x + y
    return sum #Return is used as an exit function and goes back to the place where it was called.

def subtract(x, y):
    sum = x - y
    return sum

def multiply(x, y):
    sum = x * y
    return sum

def divide(x, y):
     sum = x / y
     return sum

#function can called from other functions and programs, functions can be called by typing the function name with the appropriate parameters.
#The none function can be used if there is no expression in the statement of the return statement itself.
print("Welcome to the beta test for Emil's Calculator, would you like to test it?(Y/N)")
answer = input()
if answer == 'Yes' or answer == 'Y' or answer == 'Ya' or answer == 'YES':
    #alternate code 'if answer in ['Y', 'Yes', 'Ya', 'YES']'
    #if “y” in answer.lower()
    print('Welcome to my calculator!!!!')
    num1 = float(input('Please enter number 1: '))
    num2 = float(input('Please enter number 2: '))

    print('Choose a operation: ')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')

    operation = input('Make a selection (1/2/3/4): ')
    if operation == '1':
        print(num1, '+',  num2, '=', addition(num1, num2))
    elif operation == '2':
        print(num1, '-',  num2, '=', subtract(num1, num2))
    elif operation == '3':
        print(num1, '*',  num2, '=', multiply(num1, num2))
    elif operation == '4':
        print(num1, '/',  num2, '=', divide(num1, num2))
else:
    print('Have a good day!')
