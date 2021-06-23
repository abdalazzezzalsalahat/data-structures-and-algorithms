import pytest
from hash.hash import Hashtable

########## tests #########


def test_hash_add(): ## 1
    """[summary]
    Test if adding a key/value to your hashtable results in the value being in the data structure
    """
    # ht = Hashtable()
    # idx = ht._hash('Dario')
    # ht.add('Dario','what ever you want')
    # ll = ht.buckets[idx]
    # key = ll.head.value.find(0)
    # value = ll.head.value.find(1)
    # assert 'Dario' == key
    # assert 'what ever you want' == value
    pass

def test_hash_get(): ## 2
    """[summary]
    Retrieving based on a key returns the value stored
    """
    ht = Hashtable()
    ht.add('Saleh','what ever you want')
    actual = ht.find('Saleh')
    assert actual == 'what ever you want'

def test_return_none(): ## 3
    """[summary]
    Successfully returns None/Null for a key that does not exist in the hashtable
    """
    ht = Hashtable()
    ht.add('Ahmad','what ever you want')
    assert ht.contains('Ahmad') == True
    assert ht.contains('Farah') == False

def test_hash_handles_collisions(): ## 4
    """[summary]
    Test if key collisions are handled properly
    """
    ht = Hashtable()
    ht.add('Farah', 'what ever you want')
    ht.add('Ahmad', 'not what ever you want')
    actual = ht.find('Farah')
    assert actual == 'what ever you want'
    actual = ht.find('Ahmad')
    assert actual == 'not what ever you want'

def test_hash(): ## 6
    """[summary]
    Successfully hash a key to an in-range value
    """

    ht = Hashtable()
    hash_val = ht._hash('apple')
    assert hash_val == 654
    assert ht._hash('apple') == hash_val

######################################### Test Integer values __Comming_soon__ #########################################

