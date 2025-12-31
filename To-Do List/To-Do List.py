         # To-Do list program
# Crete list to contain tasks
tasks = []
# create the functions
# main program
def main(tasks_list):
    # Greet the user
    print(f"Welcome to Task Manager APP!\n{'-' * 27}")
    while True:
        # print options menu until user quite
        options = ['Add tasks to the list', 'Mark task as complete', 'View tasks', 'Quit'] \
            if len(tasks_list) > 0 else ['Add tasks to the list', 'Quit']
        for index, option in enumerate(options):
            print(f'{index + 1}- {options[index]}')
        # Get user choice
        choice = input('Enter number of choice: ')
        match choice:
            case '1':
                add_task(tasks_list)
            case '2':
                if not tasks_list:
                    print('Thanks for using To Do List App.')
                    break
                else:
                    mark_task_complete(tasks_list)
            case '3':
                print(f"Invalid choice, please enter number in range 1-{len(options)}") if not tasks_list else view_tasks(tasks_list)
            case '4':
                if tasks_list:
                    print('Thanks for using Task Manager App.')
                    break
                else:
                    print(f"Invalid choice, please enter number in range 1-{len(options)}")
            case _:
                print(f"Invalid choice, please enter number in range 1-{len(options)}")
# 1- add tasks to the list
def add_task(tasks_list):
    try:
        task = input('Enter the task you want to add: ').lower()
        if len(task) == 0:
            print(f"{'-'*27}\nCan't enter an empty task.\n{'-'*27}")
            return
        date = input("Enter task date(yyyy-mm-dd): ")
        date_list = date.split('-')
        if len(date_list[0]) < 4 or len(date_list[0]) > 4\
                or len(date_list[1]) > 2 or float(date_list[1]) > 12\
                or len(date_list[-1]) > 2 or float(date_list[-1]) > 31:
            print('Invalid Date, Please enter date in correct format (yyyy-mm-dd)')
            return
        for mission in tasks_list:
            if task.strip() == mission['task']:
                print(f"{'-'*20}\nThis task already in your todolist.\n{'-'*20}")
                return
        task_info = {'task': task.strip(),'date': date, 'completed': False}
        tasks_list.append(task_info)
        print(f"{'-'*40}\n({task.title()}) task added successfully.\n{'-'*40}")
    except IndexError:
        print("Please enter date in correct format (yyyy-mm-dd)")
    except ValueError:
        print("Can't enter a text value, Please enter date in correct format (yyyy-mm-dd)")
# 2- mark task as complete
def mark_task_complete(tasks_list):
    if tasks_list:
        if all(mission['completed'] for mission in tasks_list):
            print(f"{'-'*30}\nYou've finish all tasks.\n{'-'*30}")
            return
        uncompleted_tasks = [task for index, task in enumerate(tasks_list) if not task['completed']]
        print(f"{'_' * 20}\nYour uncompleted tasks:\n{'-' * 20}")
        for i, uncompleted_task in enumerate(uncompleted_tasks):
            print(f'{i+1}- {uncompleted_task['task']}')
        print("-" * 20)
        try:
            completed_task = int(input("Enter number of task you want to mark as complete: ").lower())
            if completed_task < 1 or completed_task > len(uncompleted_tasks):
                print("Invalid choice, please enter available choice.")
                return
            uncompleted_tasks[completed_task-1]['completed'] = True
            print("Task mark as completed successfully.")
            if all(mission['completed'] for mission in tasks_list):
                print(f"{'-' * 30}\nYou've finish all tasks, congratulation!🥳🥳.\n{'-' * 30}")
                return
        except ValueError:
            print("Invalid value, please enter a number.")
# 3- view tasks
def view_tasks(tasks_list):
    if tasks_list:
        print(f"{'_' * 20}\nYour tasks is:\n{'-' * 20}")
        for index, task in enumerate(tasks_list):
            print(f'{index + 1}- {("\033[9m" + task["task"] + "\033[0m") + f" ({task['date']})✔️"}') if task["completed"] else print(f'{index + 1}- {task["task"] + f" ({task['date']})❌"}')
        print('-' * 20)
    else:
        print('Your tasks list is empty')
# call main function
if __name__ == '__main__':

    main(tasks)
