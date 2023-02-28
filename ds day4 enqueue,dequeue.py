class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
             self.last.next=Node(data)
             self.last=self.last.next
    def dequeue(self):
        if self.last is None:
            return None
        else:
            to_return=self.head.next
            self.head=self.head.next
            return to_return
a_queue=queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    #by using split do will become a list,split
    do=input('what would you like to do?').split()
    operation= do[0].strip().lower()
    if operation == 'enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation == 'dequeue':
        dequeue=a_queue.dequeue()
        if dequeue is None:
            print('queue is empty')
        else:
            print('dequeued element:',int (dequeued))
    elif operation=='quit':
        break
          
          
    
            
        
            
