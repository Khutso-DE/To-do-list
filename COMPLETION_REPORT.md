# Completion Report

Branch: feat/task-count-helper

## Changes
- `ToDoList.get_task_count()`: returns the number of tasks as an int. Existing methods are unchanged.
- `run_task_list.py`: new menu option 7 shows the total task count.
- `test_task_list.py`: new unit tests for the helper.

## Verification
- `python3 -m unittest test_task_list.py -v` -> 7 tests pass.

## Notes
- `tasks.json` and `__pycache__` are not committed.
- The menu option was not run interactively.
