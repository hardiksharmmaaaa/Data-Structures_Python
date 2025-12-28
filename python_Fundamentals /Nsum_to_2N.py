## WAP that reads an integer N from user and display te sum of the numbers from N to 2N 

n=int(input("Enter the number"))
sum=0 
for i in range(n,2*n+1):
    sum+=i
print("The sum of numbers from",n,"to",2*n,"is",sum)
