class Stack:
    def __init__(self):
        self.items = [];
    
    # In the push method, we use append() to add an item to the end of the
    # stack. 
    def push(self, item):
        self.items.append(item);
    
    # In the pop method, we use pop() to remove the item at the end of the 
    # stack.  
    def pop(self):
        if not self.is_empty():
            return self.items.pop();
        else:
            raise IndexError("The stack is empty. Can't pop, lock, and drop it, if there's nothing to pop/lock/drop.");
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1];
        else:
            raise IndexError("The stack is empty. Can't peek at the top of the stack, if there's nothing to peek at.");
        
    def is_empty(self):
        return len(self.items) == 0;

stack = Stack();
print(stack.is_empty());

stack.push("FirstIn");
stack.push("SecondIn");
stack.push("ThirdIn");

print(stack.is_empty());
print(stack.peek());
print(stack.pop());
print(stack.pop());
print(stack.is_empty());