

class Node:
    '''this Class is for Node instanceeeee'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''this STack is implementing the (Stack data structure ) with common methods used with it'''
    top = None

    def __init__(self, top=None):
        ''' creates an empty Stack when instantiated.   '''
        self.top = top

    def __str__(self):
        current = self.top
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)

    def push(self, val):
        '''Method, takes val as argument and adds new node with val to the top of the stack'''

        node = Node(val)
        if self.is_empty():
            self.top = node
            node.next = self.top
            self.top = node
        
    def pop(self):
        '''Method, removes node from top of Stack, returns node's data'''

        if not self.is_empty():
            self.top = self.top.next
            timed = self.top 
            return timed.data
        return None

    def peek(self):
        '''Method, returns val of node at top of stack, doesn't remove from stack'''

        if not self.is_empty():
            return self.top.data
        return "Cannot peek an empty stack"
    
    def is_empty(self):
        '''Method, takes no argument, and returns a boolean when it checks whether Stack is empty or not'''

        if self.top == None:
            return True
        return False

