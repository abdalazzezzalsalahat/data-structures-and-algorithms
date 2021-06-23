from linked_list.linked_list import LinkedList


class Hashtable:

    def __init__(self, size = 1024):
        """[summary]
        No default inputs.
        """
        self._buckets = [None] * size

    def __str__(self):
        """
        return the content of the table as string
        """
        output = []
        for i in self._buckets:
            if i:
                current = i.head
                while current:
                    output.append(f"{current.value['key']}: {current.value['value']}")
                    current = current.next
        string_hashmap = '\n'.join(output)

        return string_hashmap

    def __iter__(self):
        ## Itersate through the hash
        for itms in self._buckets:
        ### check if the buckets are not None
            if itms:
        ##### Iterate through the list
                for val in itms:
        ##### Append the value  in the lst
                    yield val

        ### a functon that uses yield is called a generator and they are lazy

    def _hash(self, key):
        """[summary]
        Takes in an arbitrary key and returns an index in the collection.
        Args:
            key ([type]): [description]

        Returns:
            [type]: [description]
        """

        prime_value = 1999
        hashed_key = sum([ord(char) for char in key]) * prime_value
        hashed_key = hashed_key % 1024

        return hashed_key

    def add_two(self, key, value):
        """[summary]
        Hashes key, adds key and value pair to table. Handles collisions as necessary.
        Args:
            key ([type]): [description]
            value ([int]): [description]
        """

        index = self._hash(key)

        if self._buckets[index] == None:
            bucket = LinkedList()
            
        else:
            bucket = self._buckets[index]    # bucket is now a linked list
        
        bucket.append(
            {
                'key': key,
                'value': value,
            }
        )
        
        self._buckets[index] = bucket

    def find(self, key):
        """[summary]
        Takes in key and returns the value from the table. Handles collisions as necessary.

        Args:
            key ([string]): [description]

        Raises:
            KeyError: [if key not found]
            KeyError: [if key is invalid]

        Returns:
            [string]: [returns the value of hashed key]
        """
        idx = self._hash(key)
        bucket = self._buckets[idx]

        if bucket == None:
            # raise KeyError('Key not found')
            return None

        current = bucket.head

        while current:

            if current.value['key'] == key:
                return current.value['value']

            current = current.next
        
        return None
        # raise KeyError('Key not found')

    def contains(self, key):
        """[summary]
        Takes in the key and returns a boolean, indicating if the key exists in the table already.
        Args:
            key ([String]): [description]

        Returns:
            [bool]: [True if value exist, False if not]
        """

        idx = self._hash(key)
        bucket = self._buckets[idx]

        if bucket == None:
            return False

        
        current = bucket.head

        while current:

            if current.value['key'] == key:
                return True

            current = current.next

    def keys(self):
        """
        takes a key value pair and return only the keys
        """
        lst = []

        for key in self: 
            lst.append(key['key'])
        ## return the lst 
        return lst

    def entries(self):
        """
        take the hashtable and returns a list of list containing the key and its value
        """
        ## Declare a linked list to store the key and the value in 
        lst = []

        for itms in self: 
            lst.append(itms)
        ## return the lst 
        return lst



if __name__ == "__main__":
    
    ht_one = Hashtable()
    print(ht_one._hash('A'))
    ht_one.add_two('A', ["someone test", "Rst", "R U ready"])
    print(ht_one.entries())
    print(ht_one.keys())
    ht_one.add_two


