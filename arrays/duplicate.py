## making a duplicate array from an existing array 

import array as arr 

val=arr.array('i',[1,2,3,4,5])

copy_val=arr.array(val.typecode,(i for i in val))

for i in copy_val:
    print(i,end=" ")
print()