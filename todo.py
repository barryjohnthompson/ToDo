"""
Todo is a simple, clutter-free task tracking app.

TODO: 
- write to/ load from file for persistent storage
- implement CLI
"""

class Task():
    """
    Model a todo list task.
    """

    states = ["to do", "doing", "done"]

    def __init__(self, title):
        """
        Initialize task object and set title and state (default="To Do").
        """

        self.title = title
        self.state = "to do"

    
    def __str__(self):
        """
        Overload the string representation to a nicer format.
        """

        return "Title: {}\t Status: {}".format(self.title, self.state)

    
    def show(self):
        """
        Print the task object in a useful format.
        """

        print( "Title: {}, Status: {}".format(self.title, self.state) )

        return

    
    def changeState(self, state):
        """
        Update the state of the task.
        Args:
            state(string) - state to change task to
        """

        if state.lower() in self.states:
            self.state = state
        else:
            raise Exception("State not valid")

        return


class ToDoList():
    """
    Class representing a ToDo list.
    """

    def __init__(self, title):

        self.title = title
        self.tasks = []

    
    def show(self):
        """
        Print the items in this ToDo list in a useful format.
        """
        print( "{}:".format(self.title) )
        for task in self.tasks:
            print("  " + str(task))

        return
    

    def addTask(self, title):
        """
        Add a task to this to do list.
        """

        self.tasks.append( Task(title=title) )

        return


    def find(self, title):
        """
        Find a task in the to do list.
        Args:
            title(string) - the task title to search for
        """

        retTask = None
        for task in self.tasks:
            if task.title.lower() == title.lower():
                retTask = task

        if retTask == None:
            print("Requested task not found in list")

        return retTask

    
    def updateTaskState(self, taskTitle, newState):
        """
        Update the state of a task in this list.
        Args:
            taskTitle(string) - the title of the task to update
            newState(string)  - the new state of the task
        """

        task = self.find(taskTitle)
        task.changeState(state=newState)

        return
