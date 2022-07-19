class PerfectBST:
    """
    In this example we are setting up a Binary Search Tree (BST) data structure.
    The Node class below is an inner class, or inside another class.  An inner class's real 
    name is related to the outer class, BST in this case.  To create a Node object, we will 
    need to specify BST.Node.
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided. Initially
            the child links need to be set to None.
            """

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Create a function the can insert 'data' into the BST.
        If the BST is empty, then set the root node equal to the new 
        node you are adding.
        Otherwise, call on _insert to recursively find the location to insert.
        """
        if self.root is None:
            self.root = PerfectBST.Node(data)
        else:
            # Start at the root to find a place to place the new node.
            self._insert(data, self.root)

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node with 'data' inside of it.
        This function is called within the 'insert'.
        That means the BST already has a root (at minimum) and the new data needs to be placed underneath it.
        The current sub-tree is represented by 'node'.
        """
        if data < node.data:
            # If the data is less than the node it is looking at, then it belongs on the left side.
            if node.left is None:
                # There's nothing on the left so we can place it here.
                node.left = PerfectBST.Node(data)
            else:
                # Need to keep looking. Call _insert recursively on the left sub-tree until a free spot is found.
                self._insert(data, node.left)
        elif data > node.data:
            # If the data is larger than the node you are looking at than it belongs on the right side.
            if node.right is None:
                # There's nothing on the right so we can place it here.
                node.right = PerfectBST.Node(data)
            else:
                # Need to keep looking.  Call _insert recursively on the right sub-tree to find a spot.
                self._insert(data, node.right)

    def __contains__(self, data):
        """ 
        Next we need a function that can check all the data in the BST.
        This function supports the ability to use the 'in' keyword:

        if 10 in BST:
            ("10 is in the bst")

        It is calling on the '_contains' function.
        """
        # It starts the search at the root.
        return self._contains(data, self.root)

    def _contains(self, data, node):
        """
        This function will search for a node that contains the 'data' you specify.
        This function is intended to be called the first time by the __contains__ function.
        """
        # The __contains__ function already starts at the root. Check first if data is less than node.
        if data < node.data:
            if node.left is None:
                return False
            else:
                return self._contains(data, node.left)

        # If data is greater than node then look to the right.
        elif data > node.data:
            if node.right is None:
                return False
            else:
                return self._contains(data, node.right)

        # And last of all check if data is equal to the node.
        elif data == node.data:
            return True

    def __iter__(self):
        """
        You need to be able to iterate through your BST.
        Perform a forward traversal starting starting from the root of the BST.
        This is called a generator function.
        This function is called when a loop	is performed:

        for value in BST:
            print(value)

        """
        yield from self._go_forward(self.root)

    def _go_forward(self, node):
        """
        This is the function that the iterate function calls on.
        It is how the forward traversal is performed.
        It will give the numbers in ascending order.
        If the node that we are given exists,
        then we will keep traversing on the left side to get the smaller numbers first.
        Then we will provide the data in the current node.
        Finally we will traverse on the right side to get the larger numbers.

        ***
        The use of the 'yield' will allow this function to support loops
        like:

        for value in BST:
            print(value)

        The keyword 'yield' will return the value needed in the 'for' loop.
        When the 'for' loop wants to get the next value,
            the code in this function will start back up where the last 'yield' returned a value.
        The keyword 'yield from' is used when our generator function needs
        to call another function for which a `yield` will be called.  
        ***

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._go_forward(node.left)
            yield node.data
            yield from self._go_forward(node.right)

    def __reversed__(self):
        """
        Perform a backward traversal starting from the root of the BST.

        for value in reversed(BST):
            print(value)
        """
        yield from self._go_backward(self.root)

    def _go_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the BST.
        This means it will give the numbers in descending order.
        If the node that we are given exists, then we will keep traversing on the right
        side getting the larger numbers first. 
        Then we will provide the data in the current node.
        Finally we will traverse on the left side to get the smaller numbers.

        *** Uses the yield generator. ***

        This function is intended to be called the first time by the __reversed__ function.
        """
        if node is not None:
            yield from self._go_backward(node.right)
            yield node.data
            yield from self._go_backward(node.left)

    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.

        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        if node is None:
            return 0
        else:
            return 1 + max(self._get_height(node.left), self._get_height(node.right))


# Now try out your program!
print("\n=========== Insert data into the BST ===========")
tree = PerfectBST()
tree.insert(7)
tree.insert(5)
tree.insert(5)
tree.insert(10)
tree.insert(2)
tree.insert(20)
tree.insert(3)
tree.insert(4)
print("The iterate function is calling the traverse forward function.")
print("So when you tell the program to print each data node it will put them in ascending order.")
for x in tree:
    print(x)
print("Did you notice that when you are done that it does not print duplicates?")

print("\n=========== Now you can check for specific numbers inside the BST. It will give you a True or False. ===========")
print(3 in tree)
print(2 in tree)
print(7 in tree)
print(6 in tree)
print(9 in tree)

print("\n=========== Now lets print the list in descending order. ===========")
for x in reversed(tree):
    print(x)

print("=========== How tall, or how many levels, is your tree? ============")
print(tree.get_height())
