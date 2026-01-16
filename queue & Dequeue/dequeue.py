## In this code, we will implement all the queue functions 


class dequeue:
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

    def delete(self):
        if len(self.s)==0:
            raise Exception("underflow")
        else:
            return self.s.pop(0)
        
# These are the additional functions for dequeue Rest all the same in the case of queue
        
    def insert_front(self,item):
        self.s.insert(0,item)                       # inserting element at front of dequeue
    
    def delete_rear(self):
        if len(self.s)==0:
            raise Exception("underflow")           # deleting element from rear of dequeue 
        else:
            return self.s.pop()


que=dequeue()

## Now you can do the operations !! 

#adding first 5 elements in queue

que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
que.enqueue(50)

print(que.peek())
print(que.display())

que.delete()
print(que.display())
print(que.length())

# now inserting element at front
que.insert_front(100)
print(que.display())

# now deleting element from rear
que.delete_rear()
print(que.display())