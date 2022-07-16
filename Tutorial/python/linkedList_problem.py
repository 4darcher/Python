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
