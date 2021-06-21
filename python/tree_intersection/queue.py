class Node:
    '''this Class is for Node instanceeeee'''
    def __init__(self, value):
        self.value = value
        self.next = None

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
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)

    def enqueue(self, value):
        '''Method, takes any value as argument and adds node with that value to back of queue Add an item to the rear fo the queue '''

        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
            # self.rear = self.rear.next

    def dequeue(self):
        '''Method, removes node from front of queue, returns that node's value'''
        
        if not self.is_empty():
            self.front = self.front.next
            temp = self.front
            temp.next = 'Queue is empty'
            return temp.value
        return 'Queue is empty'

    def is_empty(self):
        '''Method, checks if queue is empty or not so it will return a boolean'''
        
        if self.front == None:
            return True
        return False

    def peek(self):
        '''Method, returns val of node located at front of queue, without  removing it'''

        if not self.is_empty():
            return self.front.value
        return 'Queue is empty'
