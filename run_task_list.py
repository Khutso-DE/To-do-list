from task_list import ToDoList, get_valid_int
import time
import sys


def run_application():
    """run the app"""
    print("\nWelcome to the To-do list application. Here you can add your tasks, remove them\n"
          "and update them.\n")
    App = ToDoList()

    menu = "\n---To-do List---\n1) Add task (+)\n2) Update task\n3) Remove Task\n4)Exit\n"
    running = True
    while running:
        time.sleep(1)
        App.display_tasks()
        print(menu)
        time.sleep(0.7)

        # get user selection
        option = input("Your selection\n"
                       "> ").lower().strip()

        if option == "1":
            task = input("Task: ")
            time.sleep(1)
            print(App.add_task(task))
            time.sleep(1)

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
                print(App.remove_task(task))
                time.sleep(1)

        elif option == "4":
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
