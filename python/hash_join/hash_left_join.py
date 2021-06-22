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

    # else:
    #     for element in hash_one:

    #         if element in hash_two:

    #             val_frst = hash_one.get(element)
    #             val_sec = hash_two.get(element)
    #             new_hash.add(element, [val_frst, val_sec])

    #         else:
    #             new_hash.add(element, [val_frst, None])



# def hash_intersection(hash_one, hash_two):
#     """[summary]

#     Args:
#         tree_one ([binary tree]): [unorderd]
#         tree_two ([binary tree]): [unorderd]

#     Returns:
#         [list]: [list of the intersections elemnts of the two trees]
#     """

#     if not hash_one and not hash_two:
#         return "tree is empty"
        
#     else:
#         # hash_one = hash_one.pre_order()
#         # hash_two = hash_two.pre_order()
#         lst = []
#         hash_map = Hashtable()
        
#         for element in hash_one:
#             str_el = str(element)
#             if hash_one.contains(str_el):






#         for element in hash_one:
            
#             if hash_map.contains(str_el):
#                 lst.append()

#         for element in hash_two:
#             str_el = str(element)
#             if hash_map.contains(str_el):

#             hash_map.append(str_el)

#     return hash_map


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





