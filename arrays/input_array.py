# making an array from user input 

import array as arr 

val=arr.array('i',[])

n=int(input("Enter the length of the array"))

for i in range(n):
    x=int(input("Enter the value"))
    val.append(x)
       

for i in val:
    print(i,end=" ")    
print("\n")       