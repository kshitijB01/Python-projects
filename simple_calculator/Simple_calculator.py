#Simple Calculator for Addition, Subtraction, Multiplication, Division
num1 = float(input("Enter the number 1 : "))
num2 = float(input("Enter the number 2 : "))

operation = input("Enter the type of operation : ")
if operation == "+":
    print("Solution = " , num1 + num2)
elif operation == "-":
    print("Solution = " , num1 - num2)
elif operation == "*":
    print("Solution = " , num1 * num2)
elif operation == "/":
    num2 == 0
    print("Undefined")
elif operation == "/":
    print("Solution = " , num1 / num2)
else :
    print("Calculator is not too advanced")

