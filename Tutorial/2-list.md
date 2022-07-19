# Linked Lists
  

In the previous tutorial we showed how a stack can be implemented using the python built-in class list. A list is basically a dynamic array. What that means is, we can easily add or remove an item from the list during run time without specifying any size. Inserting and deleting from an array can be time expensive because you need to move the items next to them over. By using linked lists to implement a stack the timing will be improved, no matter how big the list is. In Big O Notation the linked list is O(1), constant time. If you had a list a million long to go through, this would be a huge advantage. The growth is constant and as it looks on a graph, the y never increases as the x changes. This is the best and most efficient of data structures.  
  
  
Linked lists are comprimised of nodes. Each node stores a piece of data linked to a reference to the next and/or previous node. This builds a linear sequence of nodes. The beginning of a linked list is called the head, and the end is referred to as a tail. Unlike the stack example a linked list does not have an exact set of operations. They are data structures that are used to create other data stuctures, like stacks. We will use the operations of stack while implemented through a linked list. 

![Types of Linked Lists](/Tutorial/pictures/linkedListTypes.jpeg)

We are going to go over an example of the LIFO principle of stacks by using a linked list as the underlying storage class.  
  
    # Linked List Stack
    class LinkedList():

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
            self._size += 1

        # A function that will return true if the stack is empty and false if elements are still in it.

        def is_empty(self):
            return self._size == 0

        # Create a function that removes the last element using the pop method.
        def popElement(self):
            # check to see if the stack is empty before removing
            # raise an exception if empty
            if self.is_empty() == True:
                return print("Stack is empty, nothing to remove.")
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

        # We need to make the object iterable. If it is not then we can't
        # tell it to print the string everytime we add a new element.
        def __iter__(self):
            curr = self.head
            while curr is not None:
                yield curr.element
                curr = curr.next

        # Print a string so that you know what is in your linked list

        def __str__(self):
            output = "Your Linked List: "
            first = True
            for value in self:
                if first:
                    first = False
                else:
                    output += ", "
                output += str(value)
            output += "."
            return output

        # Now test out your program.
    newLinkedList = LinkedList()

    # Look and see if the stack is empty, should return true.
    newLinkedList.is_empty()
    # Add new nodes using the push method.
    newLinkedList.pushElement("This")
    # We are going to print the list everytime we change it so that we can see what is happening.
    print(newLinkedList)
    newLinkedList.pushToTail("is")
    print(newLinkedList)
    newLinkedList.pushToTail("a")
    print(newLinkedList)
    newLinkedList.pushToTail("linked")
    print(newLinkedList)
    newLinkedList.pushToTail("list")
    print(newLinkedList)
    # print("\n")
    # Take a look and see what the last element, or tail, is.
    # newLinkedList.peek()  # should return "list"
    # Look and see if the stack is empty, should return false.
    newLinkedList.is_empty()
    # Check how many nodes are in the linked list.
    print("How many values are in the list?")
    newVariable = newLinkedList.size()  # Should return 5
    print(newVariable)
    print("Add another value to the tail.")
    newLinkedList.pushToTail("!")
    print(newLinkedList)
    newVariable = newLinkedList.size()  # Should return 6
    print("How many values are in the list?")
    print(newVariable)
    print("Remove 7 values.")
    # Remove using the pop.
    newLinkedList.popElement()  # removes "!""
    newLinkedList.popElement()  # removes "list"
    newLinkedList.popElement()  # removes "linked"
    newLinkedList.popElement()  # removes "a"
    newLinkedList.popElement()  # removes "is"
    newLinkedList.popElement()  # removes "This"
    newLinkedList.popElement()
  
## Code's Output:
![Types of Linked Lists](/Tutorial/pictures/LinkedListOutput.png)
  
Linked lists are also great for having a list that you can insert a new node/value at the head (beginning), end (tail), or anywhere in the middle (by insert next to a node/value you tell it to). Try this example on your own. Guidelines are given to get you started. Try to solve this on your own before checkiing the answer.  
  
In this problem we are going to build list of map directions. After we already have a route we are going to add another stop in the middle of the journey. Then print the new list of directions.  
  
 

    class MapList:
        """
        Implement the LinkedList data structure. The Node class below is a class inside the MapList class. This means that Node is dependent on MapList. To create a Node object you need to call MapList.Node.
        """
        class Node:
            """
            Set up the constructor to initialize the Node. Each Node object will have links to the previous and the next node.
            """

            def __init__(self, data):
                self.data = data
                self.next = None
                self.prev = None

        def __init__(self):
            """
            This will initialize an empty linked list.
            """
            self.head = None
            self.tail = None

        def startOfDirections(self, value):
            """
            Start your list by inserting a new node at the head (beginning of the list.)
            """
            # Create a new node.
            new_node = MapList.Node(value)
            # If the list is empty then assign the new node as both head and tail.
            pass
            # If there is something in the list then the new node will be inserted at the beginning as a new head. The tail is won'tt be affected.
            pass

        def addToEnd(self, value):
            """
            Insert a new node to the tail (end).
            """
            pass

        def insert_after(self, value, new_value):
            """
            Insert a new value inside the list after the specified value you are looking for.
            """
            # Start checking for the value specified at the head.
            curr = self.head
            while curr is not None:
                pass
                # If the value is located at the tail then we need to call the insert_tail function so that the new value can be added as the new tail.
                pass
                # After checking if the value is the head or tail then look at all the other values in the list. When you find it, insert it, and connect it to the node before and after it.
                pass
                # Use a return so we can exit out of the function after the insert is done.
                return
                # Now go to the next node in the list searching for the value node.
                curr = curr.next

        def replace(self, old_value, new_value):
            """
            If you want to replace one node with another, then search for all of the 'old_value's and replace them with the 'new_value'.
            """
            curr = self.head
            pass

        def __iter__(self):
            """
            We need to make this class iterable.
            """
            # Start at the head since this is a forward iteration.
            curr = self.head
            while curr is not None:
                # Use the yield keyword provided in python. This statement returns a generator object to the one who calls the function which contains yield, instead of simply returning a value.
                pass
                # Go on to the next node in the list.
                pass

        def __str__(self):
            """
            Return a string representation of the list you are creating. This way you can see what is happening.
            """
            output = "Directions to BYU-I: \n"
            first = True
            for value in self:
                if first:
                    first = False
                else:
                    output += ", \n"
                output += str(value)
            output += " Enjoy your visit!"
            return output


    """
    Let's try it out!
    """

    print("\n======= Insert the first node, since it is empty it will assign this node as the head and the tail. =======")
    adventure = MapList()
    adventure.startOfDirections("Starting at SLC Airport")
    print("======= Insert nodes to the tail. =======\n")
    adventure.addToEnd("Get on I-80 E")
    adventure.addToEnd(
        "Follow I-15 N and US-20 E to University Blvd in Rexburg, ID")
    adventure.addToEnd("Follow University Blvd to W 1000 S / W 7th S")
    adventure.addToEnd("You have arrived.")
    print(adventure)
    """
    Directions to BYU-I: 
    Starting at SLC Airport, 
    Get on I-80 E, 
    Follow I-15 N and US-20 E to University Blvd in Rexburg, ID, 
    Follow University Blvd to W 1000 S / W 7th S, 
    You have arrived. Enjoy your visit!"""

    print("\n======= Add a stop in your trip. Insert new value after the first occurance of value you tell it to look for. =======")
    print("======= Insert new directions after the first statement. =======\n")
    adventure.insert_after(
        "Get on I-80 E", "Follow the signs to stay on I-80 E / I-15 S / UT-269 / 600 S")
    adventure.insert_after("Follow the signs to stay on I-80 E / I-15 S / UT-269 / 600 S",
                        "Take Exit 121, following signs for 600 S")
    adventure.insert_after(
        "Take Exit 121, following signs for 600 S", "Turn Left on S State St")
    adventure.insert_after("Turn Left on S State St",
                        "Turn Left on E 0 s / S Temple S")
    adventure.insert_after("Turn Left on E 0 s / S Temple S",
                        "Now go back to I-15 N")
    adventure.insert_after("Now go back to I-15 N", "Head west toward S Main St")
    adventure.insert_after("Head west toward S Main St",
                        "Merge onto S Temple until you can turn Right on W Temple")
    adventure.insert_after(
        "Merge onto S Temple until you can turn Right on W Temple", "Turn Left onto N Temple")
    adventure.insert_after("Turn Left onto N Temple", "Turn Right onto US-89 N")
    adventure.insert_after("Turn Right onto US-89 N", "Turn Right onto 600 N")
    adventure.insert_after("Turn Right onto 600 N",
                        "Merge onto I-15 N via the ramp to Ogden")
    adventure.insert_after("Merge onto I-15 N via the ramp to Ogden",
                        "Now continue on your way to Rexburg")
    print(adventure)

    print("\n======= There's an error! It needs to be replaced with the right directions. =======")
    print("\n======= Search for instances of old_value and replace with the value of new_value. =======")
    print("======= Replace the right with left when turning on 600 N. =======\n")
    adventure.replace("Turn Right onto 600 N", "Turn *Left* onto 600 N")
    print(adventure)

  
The answer can be found at: [Linked List Answer](/Tutorial/python/linkedList_solution.py)  
 