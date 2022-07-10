# Stacks
  
Each data structure serves a purpose and it is best to know the benefits of each so that you can pick the best one to solve a problem. We will start first with stacks, the simplest of all data structures. They can also be thought of as the most important. A stack is a collection of objects that are inserted and removed by following the "Last In First Out" (LIFO) principle. This means that the last item that is added, or inserted, will have to be the first object removed. The first item added will be the last to be removed. The best example of using stacks in everyday life would be the Undo function on your word processing program. Everytime you click the undo button or type 'Ctrl Z' you are calling on the stack function to remove the last item you just typed. You can not just go and undo the first item until you have removed all the other items typed after it.  
  
Big O notation is a mathematical representation of the algorithm's (or function's) performance. The O stands for order. A stack by itself has O(1) performance, except for the worse case in which the push method has an O(n). Stack function performance is based on the performance of the dynamic array. If the array is completely full then the array size needs to be changed. Then all the items must be copied from one array to another. This is why we classify a stack as O(n). If you were to graph this it would be seen as a constant increase, x = y. This is not the most efficent.
  
  
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


Now you can try to solve a problem on your own. How would you write a program that can go back each page you are browsing on the web? This is done everytime a user clicks on the back arrow that is at the top of the window or hits the Alt/Cmd + left arrow (on the keyboard). Here's a little code to get you started. Please try to figure this out on your own before looking at the answer.


    # Create an empty stack were the search history will be added to.
    # This variable is declared before the rest of the code so that it is global and can be used throughout the program.

    History = []
    def historyStack():
        Pass

    def isStackEmpty(History):
        return len(History) == 0

    # A function where the websites visited will be added.
    def addNewHistory(History, webPage):
        Pass

    # Another function can can be called to go backwards, or view previous page.
    def goBack(History):
        if (isStackEmpty(History)):
            return ("Your history is empty, you can't go back.")
        Pass

    # Function to tell user what the last page was before removing it.
    def lastPageVisited(History):
        Pass


    # Now test out your program.
    # Add a few pages to your search history:
    addNewHistory(History, "www.tutorialspoint.com")
    addNewHistory(History, "www.youtube.com")
    addNewHistory(History, "www.byui.edu")

    # Check what your last visited page is before deleting.
    # Last page visited:  www.byui.edu
    print("Last page visited: ", lastPageVisited(History))

    # Remove the last page and go back to previous.
    Pass

    # Add a few more pages.
    addNewHistory(History, "www.duckduckgo.com")
    addNewHistory(History, "www.churchofjesuschrist.org")

    # List current history.
    # Current search history:  ['www.tutorialspoint.com', 'www.youtube.com', 'www.duckduckgo.com', 'www.churchofjesuschrist.org']
    print("Current search history: ", History)

    # Remove all the pages until you have an empty stack.
    # Current search history:  []
    Pass

    print("Current search history: ", History)


The answer can be found at: [Stack Answer](/Tutorial/python/stack_solution.py)