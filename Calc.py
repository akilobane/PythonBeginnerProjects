#My First Calculator
num1 = input("Enter first number of your equation: ")
num2 = input("Enter second number of your equation: ")

equation = input('Choose between: +, -, * or /.: ')

if equation == '+':
    answer = float(num1) + float(num2)
elif equation == '-':
    answer = float(num1) - float(num2)
elif equation == '*':
    answer = float(num1) - float(num2)
elif equation == '/':
    answer = float(num1) / float(num2)

print(answer)
