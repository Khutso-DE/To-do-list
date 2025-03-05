import time


def get_valid_int() -> int:
    """get an integer input from the user"""
    while True:
        number = input("Task (enter by position/index): ")
        if number.isdigit():
            return int(number)


class ToDoList:
    """represent a to-do list application"""

    def __init__(self):
        """initializing ToDoList attributes"""
        self.tasks = []

    def add_task(self, task: str):
        """adds a task in the to-do list"""

        # confirm if the user wants to duplicate a task
        if task in self.tasks:
            confirmation = input("Task already added.\nDo you want to add it again?: ").lower().strip()
            if confirmation == 'yes' or confirmation == 'y':
                self.tasks.append(task)
                return "\nTask added.\n"
            else:
                pass
        elif task.startswith(" ") or task == "":
            return "\nNot a valid task. Perhaps the task starts with an invalid character.\n"
        else:
            self.tasks.append(task)
            return "\nTask added.\n"

    def remove_task(self, index: int, command: str):
        """removes a task by its index"""
        if index <= 0:
            return "\nThat is not a valid index.\n"

        if command.lower() == "yes" or command.lower() == "y":
            try:
                self.tasks.remove(self.tasks[index - 1])
            except IndexError:
                # return "There is no task at that index."
                return "\nThere is no task at that index.\n"
            return "\nTask removed.\n"
        else:
            return "\nTask not removed\n"

    def remove_all(self, response: str):
        """removes all the tasks at once"""

        if response.lower() == "yes" or response.lower() == "y":
            self.tasks.clear()
            return "You have no more tasks remaining."
        else:
            return "Tasks not removed."

    def display_tasks(self) -> None:
        """print the list of to-do's on the console"""
        if not self.tasks:
            print("\n--- No Tasks ---\n")
            return
        else:
            print("\n--- To-Do List ---")
            for i in range(len(self.tasks)):
                time.sleep(0.4)
                print(f"{i + 1}) {self.tasks[i]}")
            print()
        time.sleep(1)
        
    def update_task(self, index: int, changes: str):
        """update the task in the to-do list"""

        if not self.tasks:
            return "\nYou have no tasks to update.\n"

        if index <= 0:
            return "\nThat is not a valid index.\n"

        try:
            time.sleep(1)
            print(f'\nupdating "{self.tasks[index - 1]}" to "{changes}" ...\n')
            time.sleep(1)
            self.tasks[index - 1] = changes
        except IndexError:
            return "\nThere is no task at that index.\n"
        return "\nTask updated.\n"

"""
updates:
    remove all task
    create a history or back-up for all removed tasks
    add a json file
"""