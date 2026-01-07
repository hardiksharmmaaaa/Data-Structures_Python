# this code contains all the stack function implementation 

class stack:
    def __init__(self):
        self.s=[]

    def length(self):
        return len(self.s)

    def display(self):
        return self.s

    def push(self,item):
        self.s.append(item)
        
    def peek(self):
        if len(self.s)==0:
            raise Exception("Stack is empty")
        else:
            return self.s[-1]

    def pop(self):
        if len(self.s)==0:
            raise Exception("Stack is Empty")
        else:
            return self.s.pop()

stk=stack()

## Now you can do the operations !! 

#adding first 5 elements in stack 

stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
stk.push(50)

print(stk.peek())
print(stk.display())

# now poping the elements 

stk.pop()
print(stk.display())

# now checking the length of the stack 

print(stk.length())


