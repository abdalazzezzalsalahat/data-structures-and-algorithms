from math import ceil, log
 
class K_Node:
    def __init__(self, value):
        self.key = value
        self.child = []
  
def k_ary_tree(A, n, k, h, ind):
      
    if (n <= 0):
        return None
  
    nNode = K_Node(A[ind[0]])

    if (nNode == None): 
        print("Memory error") 
        return None
  
    for i in range(k):

        if (ind[0] < n - 1 and h > 1): 
            ind[0] += 1
  
            nNode.child.append(k_ary_tree(A, n, k, h - 1, ind))
        else: 
            nNode.child.append(None)
    return nNode
  
def k_ary_tree_level(A, n, k, ind):
    height = int(ceil(log(float(n) * (k - 1) + 1) / log(float(k)))) 
    return k_ary_tree(A, n, k, height, ind)
  
def postord(root, k):
    if (root == None):
        return
    for i in range(k):
        postord(root.child[i], k) 
    print(root.key, end = " ")




if __name__ == '__main__':
    ind = [0] 
    k = 3
    n = 10
    preorder = [ 1, 2, 5, 6, 7, 3, 8, 9, 10, 4] 
    root = k_ary_tree_level(preorder, n, k, ind) 
    print("Postorder traversal of constructed", "full k-ary tree is: ") 
    postord(root, k)