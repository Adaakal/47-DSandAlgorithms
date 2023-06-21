class Queue:
    def __init__(self):
        self.items = []; # initializes Queue with empty list
    
    
    # Define the methods that allow us to interact with the Queue
    
    # In the 'enqueue' method, we add an item to the end of the 
    # queue by using the 'append' menthod.
    def enqueue(self, item):
        self.items.append(item);
    
    # On the other hand, the 'dequeue' method removes the item
    # at the front of the queue by using the 'pop' method.
    # It's important to check if the queue is empty before attempting
    # to dequeue an item. An 'IndexError' will occur if the queue is empty.
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0);
        else:
            raise Exception("The queue is empty");
        
    def peek(self):
        if not self.is_empty():
            return self.items[0];
        else:
            raise IndexError("The queue is empty");
        
            
    def size(self):
        return len(self.items);
        
    def is_empty(self):
        return len(self.items) == 0;
        


queue = Queue();
print(queue.is_empty());

queue.enqueue("FirstIn");
queue.enqueue("SecondIn");
queue.enqueue("ThirdIn");

print(queue.size());
print(queue.peek());
#print(queue.dequeue());
print(queue.size());

class QueueLinkedList:
    def __init__(self):
        self.size = 0;
        self.first = None;
        self.last = None;
        self._list = LinkedList();
        
    
        