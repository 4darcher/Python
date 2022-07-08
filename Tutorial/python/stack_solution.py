"""
This is the answer to the following problem:

How would you write a program to go back each page you are browsing on the web? This is done everytime a user clicks on the back arrow that is at the top of the window or hits the Alt/Cmd + left arrow (on the keyboard).

"""
# Create an empty stack were the search history will be added to. This variable is declared before the rest of the code so that it is global and can be used throughout the program.

History = []


def historyStack():
    return History


def isStackEmpty(History):
    return len(History) == 0

# A function where the websites visited will be added.


def addNewHistory(History, webPage):
    History.append(webPage)

# Another function can can be called to go backwards, or view previous page.


def goBack(History):
    if (isStackEmpty(History)):
        return ("Your history is empty, you can't go back.")
    return History.pop()

# Function to tell user what the last page was before removing it.


def lastPageVisited(History):
    return History[-1]


# Now test out your program.
# Add a few pages to your search history:
addNewHistory(History, "www.tutorialspoint.com")
addNewHistory(History, "www.youtube.com")
addNewHistory(History, "www.byui.edu")

# Check what your last visited page is before deleting.
# Last page visited:  www.byui.edu
print("Last page visited: ", lastPageVisited(History))

# Remove the last page and go back to previous.
goBack(History)

# Add a few more pages.
addNewHistory(History, "www.duckduckgo.com")
addNewHistory(History, "www.churchofjesuschrist.org")

# List current history.
# Current search history:  ['www.tutorialspoint.com', 'www.youtube.com', 'www.duckduckgo.com', 'www.churchofjesuschrist.org']
print("Current search history: ", History)

# Remove all the pages until you have an empty stack.
# Current search history:  []
goBack(History)
goBack(History)
goBack(History)
goBack(History)
print("Current search history: ", History)
