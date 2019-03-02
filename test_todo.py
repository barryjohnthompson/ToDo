"""
Tests for the todo.py file
"""

from todo import Task, ToDoList

# task = Task(title="Do laundry")

# task.show()

tdlist = ToDoList(title="Chores")

tdlist.addTask( "Do laundry" )
tdlist.addTask( "Get groceries" )

tdlist.show()

print("\nAfter updating...\n")

tdlist.updateTaskState("Do laundry", "done")
tdlist.updateTaskState("Get groceries", "doing")

tdlist.show()