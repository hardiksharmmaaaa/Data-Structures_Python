### WAP to print one of the words "Negative", "Positive" or "Zero" based on the user input number. weither variable is negative number, positive number or zero.


num=float(input("Enter a number: "))

if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")   