# Right sided triangle pattern

"""
i=0                 *
i=1               * *
i=2             * * *
i=3           * * * *
i=4         * * * * *

"""

## Consider the pattern, in each row we have some spaces followed by stars. so we will have two inner loops, one for spaces and one for stars.

n=5 

for i in range(n):

    # printing spaces
    for j in range(i,n):
        print(" ",end=" ")

    # printing stars
    for i in range(i+1):
        print("*",end=" ")    

    print()