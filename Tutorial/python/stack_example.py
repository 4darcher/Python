# Implementing a stack data structure in Python

from inspect import stack

# Declare the Stack variable globally
Stack = []

# Start by creating a new empty stack


def createStack():
    return Stack

# Check if the stack you created is empty


def isStackEmpty(Stack):
    return len(Stack) == 0

# Add/push elements on to the stack by appending


def pushStack(Stack, element):
    Stack.append(element)
    # To keep track of each element that is appended use the print each element command
    print("New element added: ", element)

# Remove an element from the top of the stack using pop function


def popStack(Stack):
    # Need to check again if stack is empty or not
    if (isStackEmpty(Stack)):
        return ("The stack is empty and we cannot delete the element from the stack.")
    # If the stack is not empty then pop the element
    return Stack.pop()

# In order to read which element is on the top of the stack without removing it use this function


def topOfStack(Stack):
    # this will always return the last element no matter what size your stack is
    return Stack[-1]


# Watch it work! Perform the methods possible using the functions created above.

# Add Elemnets
pushStack(Stack, "Hello, ")
pushStack(Stack, "World!")
pushStack(Stack, "this")
pushStack(Stack, "is")
pushStack(Stack, "implementing")
pushStack(Stack, "a")
pushStack(Stack, "stack")
pushStack(Stack, "function.")

pushStack(Stack, 1)
pushStack(Stack, 2)
pushStack(Stack, 3)


# What is the top elemnt
print("The top element of the stack is ", topOfStack(Stack))

# Remove elements
print(popStack(Stack), "is removed from the stack")

# Print the stack after removing the element
print("What the stack looks like after removing element: ", Stack)

# Remove more elements & check what it looks like
print(popStack(Stack), "is removed from the stack")
print(popStack(Stack), "is removed from the stack")

print("What the stack looks like after removing element: ", Stack)
