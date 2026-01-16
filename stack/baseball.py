## This is a DSA 682. Baseball Game question 

'''
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.'''

class stack:
    def __init__(self):
        self.s=[]
    
    def plus(self):
        self.s.append(sum(self.s[-2:]))
    
    def double(self):
        self.s.append(self.
        1]*2)
    
    def remove(self):
        self.s.pop()
    
    def sum(self):
        return sum(self.s)
stk=stack()
operations=["5","2","C","D","+"]
for i in operations:
    if i=="+":
        stk.plus()
    elif i=="D":
        stk.double()
    elif i=="C":
        stk.remove()
    else:
        stk.s.append(int(i))
print(stk.sum())