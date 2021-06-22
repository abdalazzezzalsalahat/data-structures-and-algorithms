from hash.hash import *


def left_join_hash(hash_one, hash_two):
    
    new_hash = Hashtable()
    lst = []

    if not hash_one and hash_two:
        return new_hash
    
    else:
        


        if hash_one.buckets:
            for element in hash_one.buckets.head:
                print(element)
                val = hash_one.find(element)
                lst.append(val)

                if hash_two.contains(element):
                    val = hash_two.find(element)
                    lst.append(val)

                else:
                    lst.append(None)
                new_hash.add(element, lst)
        else: 
            return 'nothing'



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
    # print(ht_one._hash('A'))
    # ht_one.add('A', ["someone test", "Rst", "R U ready"])
    # print(ht_one._hash('911'))
    # print(ht_one.find('A'))
    # print(ht_one.find('Ab'))
    # print(ht_one.contains('C'))
    # ht_one._hash('fond')
    ht_one.add('fond', 'enamored')
    # ht_one._hash('wrath')
    ht_one.add('wrath', 'anger')
    # ht_one._hash('diligent')
    ht_one.add('diligent', 'employed')
    # ht_one._hash('guide')
    ht_one.add('guide', 'garp')
    # ht_one._hash('outfit')
    ht_one.add('outfit', 'usher')


    # ht_one.add('A', ["someone test", "Rst", "R U ready"]


    ht_two = Hashtable()
    # ht_two._hash('fond')
    # ht_two._hash('wrath')
    # ht_two._hash('diligent')
    # ht_two._hash('guide')
    # ht_two._hash('flow')

    ht_two.add('fond', 'averse')
    ht_two.add('wrath', 'delight')
    ht_two.add('diligent', 'idle')
    ht_two.add('guide', 'follow')
    ht_two.add('flow', 'jam')

    print(ht_one.find('fond'))
    print(ht_two.find('fond'))

    print(left_join_hash(ht_one, ht_two))





