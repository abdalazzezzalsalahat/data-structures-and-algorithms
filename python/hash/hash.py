from linked_list.linked_list import LinkedList


class Hashtable:

    def __init__(self, size = 1024):
        """[summary]
        No default inputs.
        """
        self.buckets = [None] * size

    def __str__(self):
        """
        return the content of the table as string
        """
        output = []
        for i in self.buckets:
            if i:
                current = i.head
                while current:
                    output.append(f"{current.value[0]}: {current.value[1]}")
                    current = current.next
        string_hashmap = '\n'.join(output)

        return string_hashmap

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

    def add(self, key, value):
        index = self._hash(key)

        if not self.buckets[index]:
          self.buckets[index] = LinkedList()
          self.buckets[index].append([key, value])

        if self.buckets[index]:
          current = self.buckets[index].head
          
          while current:

            if key == current.value[0]:
              current.value[1] = value
              break

            current = current.next

          if not current :
            self.buckets[index].append([key, value])

    def add_two(self, key, value):
        """[summary]
        Hashes key, adds key and value pair to table. Handles collisions as necessary.
        Args:
            key ([type]): [description]
            value ([int]): [description]
        """

        index = self._hash(key)

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
        idx = self._hash(key)
        bucket = self.buckets[idx]

        if bucket == None:
            # raise KeyError('Key not found')
            return None

        current = bucket.head

        while current:

            if current.value[0] == key:
                return current.value[1]

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
        bucket = self.buckets[idx]

        if bucket == None:
            return False

        
        current = bucket.head

        while current:

            if current.value[0] == key:
                return True

            current = current.next

if __name__ == "__main__":
    
    ht_one = Hashtable()
    print(ht_one._hash('A'))
    ht_one.add('A', ["someone test", "Rst", "R U ready"])
    print(ht_one._hash('911'))
    print(ht_one.find('A'))
    print(ht_one.contains('C'))
    


