from random import randint

# class node:
#     def __init__(self, value=None):  # deletion function
#         self.value=value
#         self.left_child=None
#         self.right_child=None
# #deletion function

# class binary_search_tree:

#     def __init__(self):
#         self.root=None


#     def insert(self, value):
#         if self.root==None:
#             self.root==node(value)
#         else:
#             self._insert(value, self.root)   # '_' before a function means it is private
    
#     def _insert(self, value,cur_node):

#         if value<cur_node.value:    # if the value < currentNode
#             if cur_node.left_child==None:    # if the currentNode does not have left child
#                 cur_node.left_child=node(value)     #create left child with our value
#             else:       # if the currentNode does have a left child
#                 self._insert(value, cur_node.left_child)

#         elif value>cur_node.value:
#             if cur_node.right_child ==None:
#                 cur_node.right_child=node(value)
#             else:
#                 self._insert(value, cur_node.right_child)
        
#         else:
#             print(' The value is already in tree!')

#     def print_tree(self):
#         if self.root!=None:
#             self._print_tree(self.root)
#         else:
#             print('fixxx fault') # need to debug
            

#     def _print_tree(self, cur_node):
#         if cur_node!=None:
#             self._print_tree(cur_node.left_chil)
#             print(str(cur_node.value))
#             self._print_tree(cur_node.right_child)
        


# def fill_tree(tree,num_elems=100,max_int=1000):
#     for _ in range(num_elems):
#         cur_elem = randint(0,max_int)
#         tree.insert(cur_elem)
#     return tree



# tree = binary_search_tree()
# tree = fill_tree(tree)

# tree.print_tree()

#///////////////////////////////////////////////////////////////////////////


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        # visit base and right node

    
        return elements


            


