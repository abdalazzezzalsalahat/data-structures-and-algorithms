class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def append(self, value):
        '''
        A method to append a value in the last node 
        input ==> value
        '''
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __str__(self):
        """
        A method to represent a class object as a string
        """
        current = self.head
        output = ''
        while current:
            if current:
                output += f"-> { {str(current.value)}} "
                current = current.next
            else:
                output += "Null"
        return output

    def insert(self, value):
        '''
        A method to add an node to the list 
        input ==> element
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

    def includes(self, values):
          '''
          A method to check if an element 
          exists in the list and returns a boolean (True/Flase)
          input ==> value 
          output ==> boolean 
          '''      
          if values is None:
            raise  TypeError("includes() missing 1 required positional argument: 'values' ") 
          else:
            current_node = self.head
            while current_node.next :
                if current_node.value == values:
                    return True
                else:
                    current_node = current_node.next
            return False
