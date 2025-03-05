import json
import time
import os


def get_valid_int() -> int:
    """get an integer input from the user"""
    while True:
        number = input("Task (enter by position/index): ")
        if number.isdigit():
            return int(number)


class ToDoList:
    """represent a to-do list application"""

    file = "tasks.json"

    @staticmethod
    def load_file(file_name):
        """loads the json file if it exits, otherwise return an empty dict"""
        # check if the file already exists
        if os.path.exists(file_name):
            with open(file_name, "r", errors="ignore") as f:
                return json.load(f)
        else:
            return {"tasks": []}

    @staticmethod
    def save_updates(file_name, contents: dict):
        """"save user data to a json file"""
        with open(file_name, "w", errors="ignore") as f:
            json.dump(contents, f, indent=4)

    def __init__(self):
        """initializing ToDoList attributes"""
        self.tasks = ToDoList.load_file(ToDoList.file)

    def add_task(self, task: str):
        """adds a task in the to-do list"""
        # confirm if the user wants to duplicate a task
        if task in self.tasks["tasks"]:
            self.tasks["tasks"].append(task)
            print("\nNote: That task is already available. You can modify it if necessary.\n")
            ToDoList.save_updates(ToDoList.file, self.tasks)  # save change to a json file
            return "\nTask added.\n"

        elif task.startswith(" ") or task == "":
            return "\nNot a valid task. Perhaps the task starts with an invalid character.\n"
        else:
            self.tasks["tasks"].append(task)
            ToDoList.save_updates(ToDoList.file, self.tasks)  # save changes to a json file
            return "\nTask added.\n"

    def remove_task(self, index: int, command: str):
        """removes a task by its index"""
        if index <= 0:
            return "\nThat is not a valid index.\n"

        if command.lower() == "yes" or command.lower() == "y":
            try:
                self.tasks["tasks"].remove(self.tasks["tasks"][index - 1])
            except IndexError:
                # return "There is no task at that index."
                return "\nThere is no task at that index.\n"

            ToDoList.save_updates(ToDoList.file, self.tasks)
            return "\nTask removed.\n"
        else:
            return "\nTask not removed\n"

    def remove_all(self, response: str):
        """removes all the tasks at once"""

        if response.lower() == "yes" or response.lower() == "y":
            self.tasks["tasks"].clear()
            ToDoList.save_updates(ToDoList.file, self.tasks)
            return "You have no more tasks remaining."
        else:
            return "Tasks not removed."

    def display_tasks(self) -> None:
        """print the list of to-do's on the console"""

        if not self.tasks["tasks"]:
            print("\n--- No Tasks ---\n")
            return
        else:
            print("\n--- To-Do List ---")
            for i in range(len(self.tasks["tasks"])):
                time.sleep(0.4)
                print(f'{i + 1}) {self.tasks["tasks"][i]}')
            print()
        time.sleep(1)

    def update_task(self, index: int, changes: str):
        """update the task in the to-do list"""

        if not self.tasks["tasks"]:
            return "\nYou have no tasks to update.\n"

        if index <= 0:
            return "\nThat is not a valid index.\n"

        try:
            time.sleep(1)
            print(f'\nupdating "{self.tasks["tasks"][index - 1]}" to "{changes}" ...\n')
            time.sleep(1)
            self.tasks["tasks"][index - 1] = changes
        except IndexError:
            return "\nThere is no task at that index.\n"

        ToDoList.save_updates(ToDoList.file, self.tasks)
        return "\nTask updated.\n"
