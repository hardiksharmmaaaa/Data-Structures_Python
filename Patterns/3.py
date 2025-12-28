"""
i=0     * * * * *
i=1     * * * *
i=2     * * *
i=3     * * 
i=4     *

"""

# look the pattern carefully, we just need to print n-i stars in each row (only change the columns code)

n=5 
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()    