import sys

# Initialize an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Done"  if task['done'] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

# Function to add a task to the to-do list
def add_task(task):
    tasks.append({"task": task, "done": False})
    print(f"Added task: {task}")

# Function to mark a task as done
def mark_task_done(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        print(f"Marked task {task_number} as done.")
    else:
        print("Invalid task number.")

# Function to delete a task from the to-do list
def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Deleted task: {deleted_task['task']}")
    else:
        print("Invalid task number.")

# Function to show the menu and handle user input
def show_menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as done: "))
            mark_task_done(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
if __name__ == "__main__":
    show_menu()
