## input the number and check if the integer entered is 1/2/3 digit number 

number=int(input("Enter the number"))

if number<10:
    print("1 digit number")
elif number<100:
    print("2 digit number")
elif number<1000:
    print("3 digit number")