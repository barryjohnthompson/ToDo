"""
Todo is a simple, clutter-free task tracking app.

TODO: 
- write to/ load from file for persistent storage
- implement CLI
"""

class Task():

    states = ["to do", "doing", "done"]

    def __init__(self, title):
        """
        Initialize task object and set title and state (default="To Do").
        """

        self.title = title
        self.state = "to do"

    
    def __str__(self):

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

        self.tasks.append( Task(title=title) )

        return

    
    def updateTaskState(self, taskTitle, newState):

        for task in self.tasks:
            if taskTitle.lower() == task.title.lower():
                task.changeState(state=newState)
            else:
                pass

        return