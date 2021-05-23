class Node:
    '''this Class is for Node instanceeeee'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''This stack is implementing the (Stack data structure ) with common methods used with it'''
    top = None

    def __init__(self, top=None):
        ''' creates an empty Stack when instantiated.   '''
        self.top = top

    def __str__(self):
        current = self.top
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        return "\n".join(items)

    def push(self, val):
        '''Method, takes val as argument and adds new node with val to the top of the stack'''

        node = Node(val)
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

        if self.top:
            return False
        return True

class Queue:
    '''this class implementing (Queue data structure ) with common methods used with it'''

    def __init__(self):
        '''   It creates an empty Queue when instantiated.'''
        self.front = None
        self.rear = None

    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        return "\n".join(items)

    def enqueue(self, data):
        '''Method, takes any value as argument and adds node with that value to back of queue Add an item to the rear fo the queue '''

        node = Node(data)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
            # self.rear = self.rear.next

    def dequeue(self):
        '''Method, removes node from front of queue, returns that node's data'''
        
        if not self.is_empty():
            self.front = self.front.next
            temp = self.front
            temp.next = 'Queue is empty'
            return temp.data
        return 'Queue is empty'

    def is_empty(self):
        '''Method, checks if queue is empty or not so it will return a boolean'''
        
        if self.front == None:
            return True
        return False

    def peek(self):
        '''Method, returns val of node located at front of queue, without  removing it'''

        if not self.is_empty():
            return self.front.data
        return 'Queue is empty'

if __name__ == "__main__":

  que = Queue()
  que.enqueue(50)
  que.enqueue(220)
  que.enqueue(98)

  print (que.__str__())
  print('\n\n\n\n\n\n')
  print(que.dequeue())
  print('\n\n\n\n\n\n')
  print (que.__str__())
  print('\n\n\n\n\n\n')
  print(que.peek())

