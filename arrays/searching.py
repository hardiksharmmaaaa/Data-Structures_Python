# creating a array and searching the element in it 

import array as arr 

val=arr.array("i",[])

n=int(input("Enter the number of Elements"))

for i in range(n):
    x=int(input("Enter the value"))
    val.append(x)

#Searching the element in the array 

search=int(input("Enter the element to search"))    

for i in range(n):
    if val[i]==search:
        print("Element found at index",i)
        break
else:
    print("Element not found")