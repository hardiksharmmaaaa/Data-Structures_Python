## Hill pattern (pyramid pattern)

"""
i=0         *
i=1       * * *
i=2     * * * * *
i=3   * * * * * * *
i=4 * * * * * * * * * 
"""

# consider the pattern, we have two right anged trianges joined together. so we will have two inner loops, one for spaces and two for stars.

n=5

for i in range(n):

    #Printing spaces
    for j in range(i,n):
        print(" ",end=" ")

    for j in range(i+1):
        print("*",end=" ")

    for j in range(i):
        print("*", end=" ")

    print()