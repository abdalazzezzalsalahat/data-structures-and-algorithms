class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += f"{ {str(current.value)} } ->"
            current = current.next
        return output

    def append(self, value):
        '''
        this method to append value in the last node 
        input ==> value
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

def zipLists(list1,list2):
    """
    Takes two linked lists as arguments. Zip the two linked lists together into one so that
    the nodes alternate between the two lists and return a reference to the head of the zipped list. 
    """
    nodes_counter_li1 = 0
    nodes_counter_li2 = 0
    current = list1.head
    while current != None:
        current = current.next
        nodes_counter_li1 += 1
    current = list2.head
    while current != None:
        current = current.next
        nodes_counter_li2 = nodes_counter_li2 + 1 
    if nodes_counter_li1 > nodes_counter_li2:
        l1 = list1
        l2 = list2
    else:
        l1 = list2
        l2 = list1
    current = l1.head 
    l2_current = l2.head 
    while current != None and l2_current != None: 
        l1_next = current.next
        l2_next = l2_current.next
        l2_current.next = l1_next 
        current.next = l2_current 
        current = l1_next 
        l2_current = l2_next 
    l2.head = l2_current 
    return l1.__str__()
    