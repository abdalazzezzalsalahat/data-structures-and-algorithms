from stacks_and_queues.stacks_and_queues import Node, Stack, Queue

'''required tests '''


def create_stack(nodes):
    '''Helper function to create a stack'''

    stack = Stack()
    for node in nodes:
        stack.push(node)
    return stack

def test_create_node():
    '''Can successfully create node'''

    node = Node('dario')
    assert node.value == 'dario'

###################################################################################

def test_stack_push(): ## 1
    '''Can successfully push onto a stack'''

    stack = Stack()
    stack.push('dario')
    assert stack.top.value == 'dario'

def test_stack_push_multiple(): ## 2
    '''Can successfully push multiple values onto a stack'''

    stack = Stack()
    assert stack.top == None
    stack.push(5)
    assert stack.top.value == 5
    stack.push(1)
    assert stack.top.value == 1
    stack.push(2)
    assert stack.top.value == 2

def test_stack_pop_multiple(): ## 3
    '''Can successfully pop off the stack'''

    stack = create_stack([1,2,3,4,5])
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.top.next == None

def test_peek(): ## 5
    '''Can successfully peek the next item on the stack'''

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

def test_create_empty_stack(): ## 6
    '''Can successfully instantiate an empty stack'''

    stack = Stack()
    assert stack.top == None

def test_peek_empty_stack_exception(): ## 7
    '''Calling pop or peek on empty stack raises exception'''
    
    stack = Stack()
    actual = stack.peek()
    expected = "Cannot peek an empty stack"
    assert actual == expected

def test_enqueue_to_queue(): ## 8
    '''Can successfully enqueue into a queue'''

    queue = Queue()
    queue.enqueue(1)
    actual = queue.front.value
    expected = 1
    assert actual == expected

def test_queue_enqueue_while_two_node(): ## 9
    """Add to a queue with two nodes."""
    
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.front.value == 1
    assert isinstance(queue.front.next, Node)
    assert queue.rear.value == 3
    assert queue.rear.next == None

def test_queue_dequeue(): ## 10
    '''Can successfull dequeue out a queue'''

    queue = Queue()
    queue.dequeue()
    assert queue.peek() == "Queue is empty"

def test_queue_peek(): ## 11
    '''Can successfull peek into a queue'''

    queue = Queue()
    queue.enqueue(1)
    assert queue.peek() == 1

def test_instantiate_queue(): ## 13
    '''Can successfully instantiate an empty queue'''

    queue = Queue()
    assert queue

def test_peek_empty_queue_exception(): ## 14
    '''Calling dequeue or peek on empty queue raises exception'''

    queue = Queue()
    actual = queue.peek()
    expected = "Queue is empty"
    assert actual == expected
