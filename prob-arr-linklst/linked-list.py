class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, val):
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        return None
    
    def prepend(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return None
    
    def pop(self):
        if self.head is None:
            raise Exception('List is empty')
        
        if self.head == self.tail:
            val = self.head.val
            self.head = self.tail = None
            return val
        
        val = self.head.val
        curr_node = self.head
        
        while curr_node.next != self.tail:
            curr_node = curr_node.next
        curr_node.next = None
        self.tail = curr_node
        return val         
    
    def pop_first():
        if self.head is None:
            raise Exception('List is empty')
            
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val
    
    def get(self, idx):
        # start from the head of the list
        curr = self.head 
        # the loop runs idx times      
        for _ in range(idx):
            # before we move, we check if curr is None
            # if it is, we've reached the end of the list and idx is greater than the lentgth of the list
            if curr is None:
                raise Exception('Index out of range')
            # this is how we move to next
            curr = curr.next  
            # after the loop ends, curr is the node at idx
            # if curr is none, it means idx is too large(it's equal to the length of the list)
        if curr is None: 
            raise Exception('Index out of range')
        # if we haven't raised an exception, curr is the node at idx
        return curr.val    
    
    def update(self, idx):
        curr = self.head
        for _ in range(idx):
            if curr is None:
                raise Exception('Index out of range')
            curr = curr.next
        