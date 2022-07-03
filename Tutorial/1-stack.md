# Stacks
  
Each data structure serves a purpose and it is best to know the benefits of each so that you can pick the best one to solve a problem. We will start first with stacks, the simplest of all data structures. They can also be thought of as the most important. A stack is a collection of objects that are inserted and removed by following the "Last In First Out" (LIFO) principle. This means that the last item that is added, or inserted, will have to be the first object removed. The first item added will be the last to be removed. The best example of using stacks in everyday life would be the Undo function on your word processing program. Everytime you click the undo button or type 'Ctrl Z' you are calling on the stack function to remove the last item you just typed. You can not just go and undo the first item until you have removed all the other items typed after it.  
  

Stack function performance is based on the performance of the dynamic array. Big O notation is a mathematical representation of the algorithm's (or function's) performance. In Big O Notation a stack can be written as O(1). This means that on a graph the growth is constant. Whenever x gets bigger y does not. This is consider the best and most efficent of data structural performance.

![ctrl z image](/Tutorial/pictures/ctrl_z.jpg)  

  
**Stack Methods**  
  
In order to properly implement a stack (S) function you can use the following methods:
  
- S.push(e): Adds an element (e) to the top of stack S.
- S.pop(): Removes and returns the element from the top of the stack S. If the stack is empty you will receive an error.
- S.peek() or S.top(): Returns a reference to the top of the stack S without removing it. Just like pop, you will receive an error message if it is empty.
- S.is_empty(): Returns True if no elements found in the stack S, or else it will return false.
- S.size(): Returns the number of elements in the stack S.  


We are going to use the built-in class of list in Python to represent a stack function. To push an item on to the top of the stack we will use the append function. To pop, or remove, an item we will use the pop function.  Read through the following example before trying to solve the problem at the end on your own.


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
    """
    pushStack(stack, "Hello, ")
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

    