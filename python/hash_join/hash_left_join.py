from hash.hash import *


def left_join_hash(hash_one, hash_two):
    
    new_hash = Hashtable()
    lst = []

    if not hash_one and hash_two:
        return new_hash

    for element in hash_one.buckets:
        if element:
            key = element.head.value[0]
            val = element.head.value[1]
            new_hash.add(key, [val, None]) 
    
    for element in hash_two.buckets:
        if element:
            result = new_hash.contains(element.head.value[0])
            key = element.head.value[0]
            val_one = hash_one.find(key)
            val_two = element.head.value[1]
            if result:
                new_hash.add(key, [val_one, val_two])
    
    return new_hash.__str__()



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

    print(ht_one.find('fond'))
    print(ht_two.find('fond'))
    # print(left_join(ht_one, ht_two))

    print(left_join_hash(ht_one, ht_two))





