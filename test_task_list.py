import unittest
from task_list import *


class ToDoTestCase(unittest.TestCase):
    def test_add_task(self):
        """test for valid task addition"""

        test_cases = {
            "task input": ["", " ", "accomplish task 1 before task 2", "after task 2, do task 3"],
            "valid output": "\nTask added.\n",
            "invalid output": "\nNot a valid task. Perhaps the task starts with an invalid character.\n"
        }

        my_list = ToDoList()

        for task in test_cases["task input"]:
            if task.startswith(" ") or task == "":
                self.assertEqual(my_list.add_task(task), test_cases["invalid output"])
            else:
                self.assertEqual(my_list.add_task(task), test_cases["valid output"])

    def test_remove_task(self):
        """test for task removal from the task list"""

        my_list = ToDoList()

        my_list.tasks = []
        self.assertEqual(my_list.remove_task(1), "\nThere is no task at that index.\n")

        my_list.tasks = ["Go to Gym"]
        self.assertEqual(my_list.remove_task(1), "\nTask removed.\n")
        self.assertEqual(my_list.remove_task(0), "\nThat is not a valid index.\n")
        self.assertEqual(my_list.remove_task(-1), "\nThat is not a valid index.\n")

    def test_update_task(self):
        """test for task updating from the task list"""

        my_list = ToDoList()

        test_cases = [
            {"input": 2, "changes": "Feed all pets", "output": "\nThere is no task at that index.\n"},  # i out of range
            {"input": 1, "changes": "Drive kids", "output": "\nYou have no tasks to update.\n"},  # for empty task list
            {"input": 2, "changes": "Cook", "output": "\nTask updated.\n"}  # for correct changes
        ]

        for i in range(3):  # get the test cases by index
            if i == 0:
                my_list.tasks = ["Feed the dog"]
            elif i == 1:
                my_list.tasks = []
            else:
                my_list.tasks = ["Feed the dog", "Go to the park"]

            self.assertEqual(my_list.update_task(test_cases[i]["input"],  # value as index to the task in self.tasks
                                                 test_cases[i]["changes"]  # value as the changes made to the task
                                                 ),
                             test_cases[i]["output"]  # value as the output expected
                             )
