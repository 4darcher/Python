class MapList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def startOfDirections(self, value):
        new_node = MapList.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addToEnd(self, value):
        new_node = MapList.Node(value)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, value, new_value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    self.insert_tail(new_value)
                else:
                    new_node = MapList.Node(new_value)
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                return
            curr = curr.next

    def replace(self, old_value, new_value):
        curr = self.head
        while curr is not None:
            if curr.data == old_value:
                curr.data = new_value
            curr = curr.next

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    def __str__(self):
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
