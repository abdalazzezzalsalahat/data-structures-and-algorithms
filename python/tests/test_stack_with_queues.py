from queue_with_stacks.queue_with_stacks import Psuedo_Queue
import pytest

q = Psuedo_Queue()

def test_enqueue(): ## 1
    q.enqueue('Dario')
    q.enqueue('Ahmad')
    q.enqueue('Saleh')
    q.enqueue('Farah')
    actual = q.stack_one.peek()
    assert actual == 'Farah'


def test_dequeue(): ## 2
    q.enqueue('Dario')
    q.enqueue('Ahmad')
    q.enqueue('Saleh')
    q.enqueue('Farah')
    actual = q.dequeue()
    assert actual == 'Dario'


def test_dequeue_2(): ## 3
  q = Psuedo_Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  popped = []
  for _ in range(3):
    popped.append(q.dequeue())
  assert popped == [1, 2, 3]

