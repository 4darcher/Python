# Stacks
  
Each data structure serves a purpose and it is best to know the benefits of each so that you can pick the best one to solve a problem. We will start first with stacks, the simplest of all data structures. They can also be thought of as the most important. A stack is a collection of objects that are inserted and removed by following the "Last In First Out" (LIFO) principle. This means that the last item that is added, or inserted, will have to be the first object removed. The first item added will be the last to be removed. The best example of using stacks in everyday life would be the Undo function on your word processing program. Everytime you click the undo button or type 'Ctrl Z' you are calling on the stack function to remove the last item you just typed. You can not just go and undo the first item until you have removed all the other items typed after it.  
  

![ctrl z imsge](/Tutorial/pictures/ctrl_z.jpg)  

  
**Stack Methods**  
  
In order to properly implement a stack (S) function you can use the following methods:
  
- S.push(e): Adds an element (e) to the top of stack S.
- S.pop(): Removes and returns the element from the top of the stack S. If the stack is empty you will receive an error.
- S.peek() or S.top(): Returns a reference to the top of the stack S without removing it. Just like pop, you will receive an error message if it is empty.
- S.is_empty(): Returns True if no elements found in the stack S, or else it will return false.
- S.size(): Returns the number of elements in the stack S.  


