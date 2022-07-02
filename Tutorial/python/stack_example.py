# Implementing a stack data structure in Python

from inspect import stack

# Start by creating a new empty stack


def createStack():
    Stack = []
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


def popStack(stack):
    # Need to check again if stack is empty or not
    if (isStackEmpty(stack)):
        return ("The stack is empty and we cannot delete the element from the stack.")
    # If the stack is not empty then pop the element
    return stack.pop()

# In order to read which element is on the top of the stack without removing it use this function


def topOfStack(stack):
    # this will always return the last element no matter what size your stack is
    return stack[-1]


# Watch it work. Create a new stack and perform the methods possible using the functions created above

# New Stack
newStack = createStack()

# Add Elemnets
"""pushStack(stack, "Hello, ")
pushStack(stack, "World!")
pushStack(stack, "this")
pushStack(stack, "is")
pushStack(stack, "implementing")
pushStack(stack, "a")
pushStack(stack, "stack")
pushStack(stack, "function.")"""

pushStack(stack, 1)
pushStack(stack, 2)
pushStack(stack, 3)


# What is the top elemnt
print("The top element of the stack is ", topOfStack(stack))

# Remove elements
print(popStack(stack), "is removed from the stack")

# Print the stack after removing the element
print("What the stack looks like after removing element: ", stack)
