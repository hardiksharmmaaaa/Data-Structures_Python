"""
i=0     *
i=1     * *
i=2     * * *
i=3     * * * *
i=4     * * * * *

"""

# look the pattern carefully, we just need to print i+1 stars in each row (only change the columns code)

n=5 
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
