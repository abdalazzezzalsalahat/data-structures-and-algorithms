from hash.hash import *


def left_join_hash(hash_one, hash_two):
    
    new_hash = Hashtable()

    if not hash_one and hash_two:
        return new_hash

    for element in hash_one:
        result = hash_two.find(element['key'])
        new_hash.add_two(element['key'], [element['value'], result])
    
    return new_hash




if __name__ == "__main__":
    
    ht_one = Hashtable()
    ht_one.add_two('fond', 'enamored')
    ht_one.add_two('wrath', 'anger')
    ht_one.add_two('diligent', 'employed')
    ht_one.add_two('guide', 'garp')
    ht_one.add_two('outfit', 'usher')


    ht_two = Hashtable()
    ht_two.add_two('fond', 'averse')
    ht_two.add_two('wrath', 'delight')
    ht_two.add_two('diligent', 'idle')
    ht_two.add_two('guide', 'follow')
    ht_two.add_two('flow', 'jam')
    
    print(left_join_hash(ht_one, ht_two))








