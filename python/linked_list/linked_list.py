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

    def __iter__(self):
        """
        loop over the linked list 
        """
        current = self.head
        while current:
            yield current.value
            current = current.next

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

    def insert(self, value):
        '''
        this method to adds an element to the list 
        input ==> element
        '''
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, values):
          '''
          this method to checks if an element 
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

        ###########################################################################

    def insert_before(self,value,new_value):
        '''
        adds an element to the list befor element  
        its take to element 
        first argument the value wich we will insert befor it 
        the second is the value wich we will insert 
        '''
        new_node = Node(new_value)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            if current.value == value:
                th_node = self.head
                self.head = new_node
                new_node.next = th_node
                return 
            else:
                    current = self.head
            while current.next :
                if current.next.value == value:
                    th_node = current.next
                    current.next = new_node
                    new_node.next = th_node
                    return 
                else:
                    current = current.next
            return 

    def insert_after(self, value, new_value):
        '''
        adds an element to the list after element  
        its take to element 
        first argument the value wich we will insert after it 
        the second is the value wich we will insert 
        '''
        new_node = Node(new_value)
        current = self.head
        if not self.head:
                self.head = new_node
        else:
            current = self.head
            while current.next != None:
                if current.next.value == value:
                    current = current.next
                    old_node = current.next
                    current.next = new_node
                    new_node.next = old_node
                    return 
                else:
                    current = current.next
            return


        ###########################################################################

    def kth_from_end(self, k):
        """takes in a value(k) and returns the Node k places away from the tail"""
        current = self.head
        arr = []
        if k < 0:
            return 'index can\'t be less the zero'
        while current:
            arr.append(current)
            current = current.next
        if len(arr) < k:
            return 'index not found'
        arr.reverse()
        if k == len(arr):
            k = k -1
        return arr[k].value
        
    #################################################################

    def kth_from_end_second(self, k):
        current = self.head
        count = 0
        while (current):
            if (count == k):
                return current.value
            count += 1
            current = current.next

    #################################################################

    def deleteNode(self, k):
        temp = self.head

        if (temp is not None):
        
            if (temp.value == k):
                self.head = temp.next
                temp = None
                return
        
        while(temp is not None):
        
            if temp.value == k:
                break
        
            prev = temp
            temp = temp.next
        
        if(temp == None):
            return
        
        prev.next = temp.next
        temp = None



if __name__ == "__main__":

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(12)
    ll.append(232)
    ll.append(324)
    ll.append(14235)
    ll.append(22366)
    ll.append(3234)
    ll.append(134)
    ll.append(2545)
    ll.append(367)
    print(str(ll))
    ll.deleteNode(22366)
    ll.deleteNode(1)
    ll.deleteNode(324)
    ll.deleteNode(367)
    print(str(ll))


