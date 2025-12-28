## WAP To print the square root for the every alternate number in the range of given input numbers 

start=int(input("Enter the starting number"))
end=int(input("Enter the ending number"))

for i in range(start,end+1,2):
    print("Square root of",i,"is",i**0.5)