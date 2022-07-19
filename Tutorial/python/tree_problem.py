class PerfectBST:

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = PerfectBST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = PerfectBST.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = PerfectBST.Node(data)
            else:
                self._insert(data, node.right)

    def __iter__(self):
        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._get_height(node.left), self._get_height(node.right))


"""
We are going to use all the code from the example and determine how to create a perfectly balance binary tree.
"""


def create_bst(sorted_list):
    """
    Given a sorted list (sorted_list), create a balanced BST.  If
    the values in the sorted_list were inserted in order from left
    to right into the BST, then it would resemble a linked list (unbalanced).
    To get a balanced BST, the _insert_middle function is called to
    find the middle item in the list to add first to the BST.  The
    _insert_middle function takes the whole list but also takes a
    range (first to last) to consider.  For the first call, the full
    range of 0 to len()-1 used.
    """
    bst = PerfectBST()  # Create an empty BST to start with
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst


def _insert_middle(sorted_list, first, last, bst):
    """
    This function will attempt to insert the item in the middle
    of 'sorted_list' (object of the create_bst function) into the 'bst' tree (defined in create_bst).
    The middle is determined by using indicies represented by 'first' and 'last'.
    For example, if the function was called on:

    sorted_list = [1, 2, 3, 4, 5, 6, 7]
    first = 0
    last = 6

    then the value 4 (index 3 which is the middle) would be added
    to the 'bst' (the insert function above can be used to do this).

    Subsequent recursive calls are made to insert the middle from the values
    before 4 and the values after 4.  If done correctly, the order
    in which values are added (which results in a balanced bst) will be:

    4, 2, 1, 3, 6, 5, 7

    This function is intended to be called the first time by
    create_bst.

    The purpose for having the first and last parameters is so that we do
    not need to create new sublists when we make recursive calls.
    Avoid using list slicing to create sublists to solve this problem.

    """
    # base case needs to check if bst is empty
    if len(sorted_list) == 0:
        pass
    # base case also needs to check if there is a single item to place in a tree
    elif len(sorted_list) == 1:
        pass
    # otherwise you need to figure out how to find the middle value
    # assign how to handle the left side and then right
    else:
        # take the list and divide by 2. Look at the left side first and place smallest first then go to next.
        # don't forget what function and objects in it you are working with:
        #  _insert_middle(sorted_list, first, last, bst)
        mid = first + last // 2
        pass
        # base cases
        pass
        # left sides split
        pass
        # right side
        pass
    return sorted_list


balancedTree1 = create_bst(
    [1, 2, 3, 4, 5, 6, 7])
singleTree = create_bst([42])
emptyTree = create_bst([])
print(balancedTree1.get_height())  # 3
print(singleTree.get_height())  # 1
print(emptyTree.get_height())  # 0
