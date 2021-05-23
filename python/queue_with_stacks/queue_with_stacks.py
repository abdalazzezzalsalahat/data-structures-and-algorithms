from python.stacks_and_queues.stacks_and_queues import Stack

class Psuedo_Queue:

    def __init__(self): 
        self.stack = Stack()


    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        return "\n".join(items)


    def enqueue(self, data):
        self.stack.push(data)


    def dequeue(self):
        reverse_stack = Stack()

        while self.stack.top:
            reverse_stack.push(self.stack.pop())
        removed = reverse_stack.pop()

        while reverse_stack.top:
            self.enqueue(reverse_stack.pop())

        return removed


if __name__ == "__main__":

    q_s = Psuedo_Queue()
    q_s.enqueue(5)
    q_s.enqueue(55)
    q_s.enqueue(555)
    q_s.enqueue(5555)

    

    q_s.dequeue()

    print(q_s.__str__())

