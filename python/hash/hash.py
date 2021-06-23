from linked_list.linked_list import LinkedList


class Hashtable:

    def __init__(self, size = 1024):
        """[summary]
        No default inputs.
        """
        self._buckets = [None] * size

    def __str__(self):
        """[summary]
            return the content of the table as string
        Returns:
            [string]: [a string ]
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
        """[summary]
            a magic function to loop over the hash
        Yields:
            [val]: [key value pairs]
        """
        for itms in self._buckets:
            if itms:
                for val in itms:
                    yield val

        ### a functon that uses yield is called a generator and they are lazy

    def _hash(self, key):
        """[summary]
        Takes in an arbitrary key and returns an index in the collection.
        Args:
            key ([string]): [description]

        Returns:
            [hashed_key]: [a hashed key]
        """

        prime_value = 1999
        hashed_key = sum([ord(char) for char in key]) * prime_value
        hashed_key = hashed_key % 1024

        return hashed_key

    def add(self, key, value):
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

        Returns:
            [string]: [returns the value of hashed key]
        """
        idx = self._hash(key)
        bucket = self._buckets[idx]

        if bucket == None:
            return None

        current = bucket.head

        while current:

            if current.value['key'] == key:
                return current.value['value']

            current = current.next
        
        return None

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
        """[summary]
            takes a key value pair and return only the keys
        Returns:
            [lst]: [list of all keys in a hash]
        """
        lst = []

        for key in self: 
            lst.append(key['key'])
        return lst

    def entries(self):
        """[summary]
        take the hashtable and returns a list of list containing the key and its value
        Returns:
            [lst]: [a list of keys and values]
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
    ht_one.add('A', ["someone test", "Rst", "R U ready"])
    print(ht_one.entries())
    print(ht_one.keys())
    ht_one.add('klsdjk')


