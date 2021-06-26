from collections import deque



class Queue():

    def __init__(self) -> None:
        """[summary]
        initializing a Queue object
        """
        self.dq = deque()
        
    def enqueue(self, value):
        """[summary]
        adding element to a Queue
        Args:
            value ([string]): [the value to be added into a queue]
        """
        self.dq.appendleft(value)

    def dequeue(self):
        """[summary]
        removing element from a Queue
        Returns:
            [string]: [the value of removed element]
        """
        return self.dq.pop()

    def __len__(self):
        """[summary]
        calculates the length of a Queue
        Returns:
            [int]: [length of a Queue]
        """
        return len(self.dq)
