### WAP That accepts two integers from the user and prints a message saying if the first number is divisible by the second number or not.

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

if num2%num1==0:
    print(num1,"is divisible by",num2)
else:
    print(num1,"is not divisible by",num2)