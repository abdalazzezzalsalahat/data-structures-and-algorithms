from stacks_and_queues.stacks_and_queues import Stack

class Psuedo_Queue:

    def __init__(self): 
        self.stack_one = Stack()
        self.stack_two = Stack()


    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)


    def enqueue(self, value):
        self.stack_one.push(value)


    def dequeue(self):
        while not self.stack_one.is_empty() : 
            self.stack_two.push(self.stack_one.pop())
        if self.stack_two.is_empty ( ) :
            raise RuntimeError('cannot dequeue  from empty stack!!') 
        return self.stack_two.pop()


if __name__ == "__main__":

    q_s = Psuedo_Queue()
    q_s.enqueue(5)
    q_s.enqueue(55)
    q_s.enqueue(555)
    q_s.enqueue(5555)

    q_s.dequeue()
    
    print(q_s.__str__())

