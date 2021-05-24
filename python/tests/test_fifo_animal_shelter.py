from stacks_and_queues.stacks_and_queues import Queue
from fifo_animal_shelter.fifo_animal_shelter import Fifo_Animal_Shelter, Node

def test_enqueue_animal(): ## 1
    shelter = Queue()
    shelter.enqueue('Dog')
    shelter.enqueue('Cat')
    shelter.enqueue('Dog')
    shelter.enqueue('Dog')
    shelter.enqueue('Cat')

    assert shelter.front.value == "Dog"
    assert shelter.rear.value == "Cat"

def test_dequeue_animal_no_pref(): ## 2
  shelter = Fifo_Animal_Shelter()
  shelter.enqueue_animal('Dog')
  shelter.enqueue_animal('Cat')
  shelter.enqueue_animal('Dog')
  shelter.enqueue_animal('Dog')
  shelter.enqueue_animal('Cat')

  assert shelter.dequeue_animal() == "Cat"

def test_dequeue_animal_with_pref(): ## 3
  shelter = Fifo_Animal_Shelter()
  shelter.enqueue_animal('Dog')
  shelter.enqueue_animal('Cat')
  shelter.enqueue_animal('Dog')
  shelter.enqueue_animal('Dog')
  shelter.enqueue_animal('Cat')

  shelter.dequeue_animal('Cat')
  assert shelter.__str__() == "Dog\nDog\nDog\nCat"

