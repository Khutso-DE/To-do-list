import unittest
from task_list import *


class ToDoTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.my_list = ToDoList()
        self.commands = ["yes", "Y", "y"]

    def test_add_task(self):
        """test for valid task addition"""

        test_cases = {
            "task input": ["", " ", "accomplish task 1 before task 2", "after task 2, do task 3"],
            "valid output": "\nTask added.\n",
            "invalid output": "\nNot a valid task. Perhaps the task starts with an invalid character.\n"
        }

        for task in test_cases["task input"]:
            if task.startswith(" ") or task == "":
                self.assertEqual(self.my_list.add_task(task), test_cases["invalid output"])
            else:
                self.assertEqual(self.my_list.add_task(task), test_cases["valid output"])

    def test_remove_all_task(self):
        """test clearing of all tasks"""

        self.my_list.tasks["tasks"] = ["Make the bed", "read for 2hrs"]
        self.my_list.remove_all("yes")
        self.assertEqual(self.my_list.tasks["tasks"], [])

        # when the user enters a response that is not a yes
        self.my_list.tasks["tasks"] = ["Make the bed", "read for 2hrs", "Eat"]
        self.assertEqual(self.my_list.remove_all("no"), "Tasks not removed.")
        self.assertEqual(self.my_list.tasks["tasks"], ["Make the bed", "read for 2hrs", "Eat"])

        for command in self.commands:
            self.my_list.tasks["tasks"] = ["Go the gym", "feed the pets", "Cook rice"]
            self.assertEqual(self.my_list.remove_all(command), "You have no more tasks remaining.")

    def test_remove_task(self):
        """test for task removal from the task list"""

        self.my_list.tasks["tasks"] = []
        for command in self.commands:  # when the are no tasks
            self.assertEqual(self.my_list.remove_task(1, command), "\nThere is no task at that index.\n")

        for command in self.commands:
            self.my_list.tasks["tasks"] = ["Go to Gym"]
            self.assertEqual(self.my_list.remove_task(1, command), "\nTask removed.\n")
            self.assertEqual(self.my_list.remove_task(0, command), "\nThat is not a valid index.\n")
            self.assertEqual(self.my_list.remove_task(-1, command), "\nThat is not a valid index.\n")

    def test_update_task(self):
        """test for task updating from the task list"""

        test_cases = [
            {"input": 2, "changes": "Feed all pets", "output": "\nThere is no task at that index.\n"},  # i out of range
            {"input": 1, "changes": "Drive kids", "output": "\nYou have no tasks to update.\n"},  # for empty task list
            {"input": 2, "changes": "Cook", "output": "\nTask updated.\n"}  # for correct changes
        ]

        for i in range(3):  # get the test cases by index
            if i == 0:
                self.my_list.tasks["tasks"] = ["Feed the dog"]
            elif i == 1:
                self.my_list.tasks["tasks"] = []
            else:
                self.my_list.tasks["tasks"] = ["Feed the dog", "Go to the park"]

            self.assertEqual(self.my_list.update_task(test_cases[i]["input"],  # value as index to the task in
                                                      # self.tasks
                                                      test_cases[i]["changes"]  # value as the changes made to the task
                                                      ),
                             test_cases[i]["output"]  # value as the output expected
                             )
