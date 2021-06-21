from .linked import LinkedList



class Hashtable:

    def __init__(self, size = 1024):
        """[summary]
        No default inputs.
        """
        self.buckets = [None] * size

    def hash(self, key):
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

    def add(self, key, value):
        """[summary]
        Hashes key, adds key and value pair to table. Handles collisions as necessary.
        Args:
            key ([type]): [description]
            value ([int]): [description]
        """

        index = self.hash(key)

        if self.buckets[index] == None:
            bucket = LinkedList()
            
        else:
            bucket = self.buckets[index]    # bucket is now a linked list
        
        bucket.append(
            {
                'key': key,
                'value': value,
            }
        )
        
        self.buckets[index] = bucket

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
        idx = self.hash(key)
        bucket = self.buckets[idx]

        if bucket == None:
            raise KeyError('Key not found')

        current = bucket.head

        while current:

            if current.value['key'] == key:
                return current.value['value']

            current = current.next
        
        raise KeyError('Key not found')

    def contains(self, key):
        """[summary]
        Takes in the key and returns a boolean, indicating if the key exists in the table already.
        Args:
            key ([String]): [description]

        Returns:
            [bool]: [True if value exist, False if not]
        """

        idx = self.hash(key)
        bucket = self.buckets[idx]

        if bucket == None:
            return False

        
        current = bucket.head

        while current:

            if current.value['key'] == key:
                return True

            current = current.next




