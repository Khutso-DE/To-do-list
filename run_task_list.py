from task_list import *
import time
import sys


def run_application():
    """run the app"""
    print("\nWelcome to the To-do list application. Here you can add your tasks, remove them\n"
          "and update them.\n")
    App = ToDoList()

    menu = "\n---OPTIONS---\n1) Add task (+)\n2) Update task\n3) Remove Task (-)\n4) Remove all tasks\n5) Exit (x)\n"
    running = True
    while running:
        time.sleep(1)
        App.display_tasks()
        time.sleep(0.7)
        print(menu)
        time.sleep(0.7)

        # get user selection
        option = input("Your selection\n"
                       "> ").lower().strip()

        if option == "1":
            task = input("Task: ")
            time.sleep(0.8)
            print(App.add_task(task))
            time.sleep(0.8)

        elif option == "2":
            # make sure user enters a valid input
            task_position = get_valid_int()
            time.sleep(0.7)
            changes = input("Enter your changes below:\n"
                            "> ")
            time.sleep(1)
            print(App.update_task(task_position, changes))
            time.sleep(1)

        elif option == "3":
            if App.tasks:
                task = get_valid_int()
                time.sleep(1)
                command = input("Are you sure you want to remove the task? (Y/N): ").lower().strip()
                print(App.remove_task(task, command))
                time.sleep(1)

        elif option == "4":
            if App.tasks:
                # get user confirmation
                response = input("WARNING: You are about to remove all your tasks! This action cannot be reversed.\n"
                                 "Are you sure? (Y/N): ").lower().strip()
                time.sleep(0.8)
                print(App.remove_all(response))
                time.sleep(0.8)

        elif option == "5":
            print("App closed...")
            running = False

        else:
            time.sleep(0.7)
            print("That is not a valid option")
            time.sleep(0.7)


if __name__ == '__main__':
    try:
        run_application()
    except KeyboardInterrupt:
        sys.exit()
