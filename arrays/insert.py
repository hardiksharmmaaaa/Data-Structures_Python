import array as arr 

val=arr.array('i',[1,2,3,4,5])

val.insert(5,6)
for i in val:
    print(i,end=" ")
print()

# using append function 

val.append(7)
for i in val:
    print(i,end=" ")
print() 