# Linked Lists
  

In the previous tutorial we showed how a stack can be implemented using the python built-in class list. A list is basically a dynamic array. What that means is, we can easily add or remove an item from the list during run time without specifying any size. Inserting and deleting from an array can be time expensive because you need to move the items next to them over. By using linked lists to implement a stack the timing will be improved, no matter how big the list is. In Big O Notation the linked list is O(1), constant time. If you had a list a million long to go through, this would be a huge advantage. The growth is constant and as it looks on a graph, the y never increases as the x changes. This is the best and most efficient of data structures.  
  
  
Linked lists are comprimised of nodes. Each node stores a piece of data linked to a reference to the next and/or previous node. This builds a linear sequence of nodes. The beginning of a linked list is called the head, and the end is referred to as a tail. Unlike the stack example a linked list does not have an exact set of operations. They are data structures that are used to create other data stuctures, like stacks. We will use the operations of stack while implemented through a linked list. 

![Types of Linked Lists](/Tutorial/pictures/linkedListTypes.jpeg)

We are going to go over an example of the LIFO principle of stacks by using a linked list as the underlying storage class.
    # Linked List Stack
    class LinkedList:

        # Create a nested node class to store the data and a reference to the next node.
        class LinkedListNode:
            # Initialize the node using the __init__ function.
            # It is called whenever an object is created from a class
            def __init__(self, e):
                self.element = e
                self.next = None
                self.prev = None

        # Initialize the empty linked list that you can manipulate later.
        def __init__(self):
            self._size = 0
            self.head = None
            self.tail = None

        # To add an element to the top of the stack use the push method.
        # The newest element is inserted at the head.
        def pushElement(self, value):
            # Create new node
            newest = LinkedList.LinkedListNode(value)
            # If and else statement to look for empty list and
            # point head and tail to the new node.
            if self.head is None:
                self.head = newest
                self.tail = newest
            # If not empty then only the self.head needs to be affected
            else:
                # Connect the new node to the previous head
                newest.next = self.head
                # And connect the previous head to the new node
                self.head.prev = newest
                # Then update the head to point to the newest node
                self.head = newest
                # Increase size of linked list by one
                self._size += 1

        # Insert a new node at the tail
        def pushToTail(self, value):
            newest = LinkedList.LinkedListNode(value)
            if self.tail is None:
                self.tail = newest
                self.head = newest
            else:
                newest.prev = self.tail
                self.tail.next = newest
                self.tail = newest

        # A function that will return true if the stack is empty and false if elements are still in it.
        def is_empty(self):
            return self._size == 0

        # Create a function that removes the last element using the pop method.
        def popElement(self):
            # check to see if the stack is empty before removing
            # raise an exception if empty
            if self.is_empty():
                raise IndexError("Stack is empty, nothing to remove.")
            elif self.head == self.tail:
                self.head = None
                self.tail = None
            elif self.tail is not None:
                self.tail.prev = None
                self.tail = self.tail.prev

            self._size -= 1

        # Look to see what the top element is without removing it.

    # Create a function that will tell you how many elements are in the stack.

        def size(self):
            return self._size

        # Print a string so that you know what is in your linked list
        def __str__(self):
            output = "Your linked List: "
            first = True
            for value in self:
                if first:
                    first = False
                else:
                    output += ", "
            output += "."
            return output

        # Now test out your program.
    newLinkedList = LinkedList()

    # Look and see if the stack is empty, should return true.
    newLinkedList.is_empty()
    # Add new nodes using the push method.
    newLinkedList.pushElement("This")
    newLinkedList.pushToTail("is")
    newLinkedList.pushToTail("a")
    newLinkedList.pushToTail("linked")
    newLinkedList.pushToTail("list")
    # Take a look and see what the last element, or tail, is.
    # newLinkedList.peek()  # should return "list"
    # Look and see if the stack is empty, should return false.
    newLinkedList.is_empty()
    # Check how many nodes are in the linked list.
    newLinkedList.size()  # Should return 5
    newLinkedList.pushElement("!")
    # Rwmove using the pop.
    newLinkedList.popElement()  # removes "!""
    # newLinkedList.popElement()  # removes "list"
    # newLinkedList.popElement()  # removes "linked"
    # newLinkedList.popElement()  # removes "a"
    # newLinkedList.popElement()  # removes "is"
    # newLinkedList.popElement()  # removes "This"
    # newLinkedList.popElement()



