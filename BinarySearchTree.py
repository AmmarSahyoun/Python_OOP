class node:
    def __init__(self, value=None):  # deletion function
        self.value=value
        self.left_child=None
        self.right_child=None
#deletion function

class binary_search_tree:

    def __init__(self):
        self.root=None


    def insert(self, value):
        if self.root==None:
            self.root==node(value)
        else:
            self._insert(value, self.root)   # '_' before a function means it is private
    
    def _insert(self, value,cur_node):
        if value<cur_node.value:    # if the value < currentNode
            if cur_node.left_child==None:    # if the currentNode does not have left child
                cur_node.left_child=node(value)     #create left child with our value
            else:       # if the currentNode does have a left child
                self._insert(value, cur_node.left_child)
