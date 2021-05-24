from stacks_and_queues.stacks_and_queues import Node, Stack, Queue


class Fifo_Animal_Shelter:
    """
    A class to adopt or donate animals (Cat's & Dog's)
    """

    def __init__(self):
        self.front = None
        self.queue = Queue()
    
    def __str__(self):
        current = self.queue.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)

    def enqueue_animal(self, animal):

        if animal == 'Dog' or animal == 'Cat':
            print(f'Thanks for dropping off your {animal}')
            self.queue.enqueue(animal)
            return 
        raise Exception('Invalid entry. Only Dogs and Cats allowed')

    def dequeue_animal(self, pref = None):
        
        if pref == None:
            adopted = self.queue.dequeue()
            print(f'Congrats on our new adopted {adopted}')
            return adopted
        elif pref == 'Cat' or pref == 'Dog':
            current = self.queue.front
            while current.next is not None and current.next.value != pref:
                current = current.next
            if current.next is None:
                print (f'Sorry, we are out of {pref}\'s')
            else:
                print('current', current.next.value)
                adopted = current.next
                current.next = current.next.next
                return adopted
        else: 
            print(f'Sorry, don\'t have any {pref}\'s. We only have Cats & Dogs')
            return None




if __name__ == "__main__":

    animal_shelter = Fifo_Animal_Shelter()
    animal_shelter.enqueue_animal('Cat')
    animal_shelter.enqueue_animal('Cat')
    animal_shelter.enqueue_animal('Cat')
    animal_shelter.enqueue_animal('Dog')

    animal_shelter.dequeue_animal('Cat')
    animal_shelter.dequeue_animal('Dog')
    

    print(animal_shelter.__str__())
    print(animal_shelter.front.value)
