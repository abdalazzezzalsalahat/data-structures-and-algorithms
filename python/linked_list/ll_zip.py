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
        if value is None:
            raise  TypeError("insert() missing 1 required positional argument: 'value' ") 
        else:
            new_node = Node(value)
            if not self.head:
                self.head = new_node
            else:
                new_node = Node(value)
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

def zipLists(list1,list2):
    """
    Takes two linked lists as arguments. Zip the two linked lists together into one so that
    the nodes alternate between the two lists and return a reference to the head of the zipped list. 
    """
    if not list1 :
        return list1 
    if not list2 :
        return list1 
    output =LinkedList()
    current1 =list1.head
    current2 =list2.head
    while current1 :
        output.append(current1.value)
        if current2 :
            output.append(current2.value)
            current2 = current2.next
        current1= current1.next
    while current2 :
        output.append(current2.value)
        current2 =current2.next
    return output.__str__()



if __name__ == "__main__":
    majd = LinkedList()
    majd.append(1)
    majd.append(2)
    ahmad = LinkedList()
    ahmad.append(5)
    ahmad.append(10)