
# A simple console-based To-Do List application with file persistence
TASK_FILE = "tasks.txt"
# Load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass  # File will be created when saving
    return tasks

# Save tasks to file

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display all tasks

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks added yet.")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Add a new task

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

# Remove a task

def remove_task(tasks):
    view_tasks(tasks)
    
    if not tasks:
        return
    
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")


# Main Menu Loop

def main():
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Exiting To-Do app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
