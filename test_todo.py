"""
Tests for the todo.py file
"""

from todo import Task, ToDoList

def test_CreateTask():
    
    task = Task(title="Do laundry")

    assert isinstance(task, Task)
    assert task.title == "Do laundry"

    return


def test_CreateToDoList():

    tdList = ToDoList(title="Chores")

    assert isinstance(tdList, ToDoList)
    assert tdList.title == "Chores"

    return


def test_AddTaskToList():

    td = ToDoList("Work")

    td.addTask("Get promotion")
    td.addTask("Do the thing")
    td.addTask("Set up meeting with Bob")

    assert len(td.tasks)== 3

    return


def test_FindTaskInList():

    td = ToDoList("Chores")

    td.addTask("Get promotion")
    td.addTask("Do the thing")
    td.addTask("Set up meeting with Bob")

    task = td.find("Get promotion")

    assert task.title == "Get promotion"

    return


def test_DefaultStateSet():

    td = ToDoList("Chores")

    td.addTask("Hoover floor")

    assert td.find("Hoover floor").state == "to do"

    return


def test_UpdateState():

    td = ToDoList("Chores")

    td.addTask("Wash dishes")

    td.updateTaskState(taskTitle="Wash dishes", newState="done")

    assert td.find("Wash dishes").state == "done"

    return
