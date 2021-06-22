from .tree import TNode, Binary_Tree

from .hash import Hashtable

def tree_intersection(tree_one, tree_two):
    """[summary]

    Args:
        tree_one ([binary tree]): [unorderd]
        tree_two ([binary tree]): [unorderd]

    Returns:
        [list]: [list of the intersections elemnts of the two trees]
    """

    if not tree_one and not tree_two:
        return "tree is empty"
        
    else:
        tree_one = tree_one.pre_order()
        tree_two = tree_two.pre_order()
        lst = []
        hash_map = Hashtable()
        
        for element in tree_one:
            str_el = str(element)
            if not hash_map.contains(str_el):
                hash_map.add(str_el, '1')

        for element in tree_two:
            str_el = str(element)
            if hash_map.contains(str_el):
                lst.append(str_el)

    return lst



if __name__ == "__main__":
    bt = Binary_Tree()
    bt.root = TNode(125)
    bt.root.left = TNode(150)
    bt.root.right = TNode(100)
    bt.root.left.left = TNode(75)
    bt.root.left.right = TNode(350)
    bt.root.right.left = TNode(90)
    bt.root.right.right = TNode(10)
    bt.root.right.right.right = TNode(10)

    bt_two = Binary_Tree()
    bt_two.root = TNode(100)
    bt_two.root.left = TNode(20)
    bt_two.root.right = TNode(75)
    bt_two.root.left.left = TNode(350)
    bt_two.root.left.right = TNode(10)
    bt_two.root.right.left = TNode(35)
    bt_two.root.right.right = TNode(200)


    
    print(tree_intersection(bt,bt_two))

