from hash.hash import *


def left_join_hash(hash_one, hash_two):
    
    new_hash = Hashtable()

    if not hash_one and hash_two:
        return new_hash

    for element in hash_one:
        result = hash_two.find(element['key'])
        new_hash.add(element['key'], [element['value'], result])
    
    return new_hash


if __name__ == "__main__":
    
    ht_one = Hashtable()
    ht_one.add('fond', 'enamored')
    ht_one.add('wrath', 'anger')
    ht_one.add('diligent', 'employed')
    ht_one.add('guide', 'garp')
    ht_one.add('outfit', 'usher')


    ht_two = Hashtable()
    ht_two.add('fond', 'averse')
    ht_two.add('wrath', 'delight')
    ht_two.add('diligent', 'idle')
    ht_two.add('guide', 'follow')
    ht_two.add('flow', 'jam')
    
    print(left_join_hash(ht_one, ht_two))

