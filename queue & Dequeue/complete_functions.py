## In this code, we will implement all the queue functions 


class queue:
    def __init__(self):
        self.s=[]

    def length(self):
        return len(self.s)

    def display(self):
        return self.s

    def enqueue(self,item):
        self.s.append(item)
        
    def peek(self):
        if len(self.s)==0:
            raise Exception("underflow")
        else:
            return self.s[-1]

    def dequeue(self):
        if len(self.s)==0:
            raise Exception("underflow")
        else:
            return self.s.pop(0)

que=queue()

## Now you can do the operations !! 

#adding first 5 elements in queue

que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
que.enqueue(50)

print(que.peek())
print(que.display())

que.dequeue()
print(que.display())
print(que.length())