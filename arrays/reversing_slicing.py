## making an array 

import array as arr

val=arr.array('i',[1,2,3,4,5])  
for i in val:
    print(i,end=" ")
# reversing an array 
print("\n")
abc=val[::-1]
for i in abc:
    print(i,end=" ")
print()    