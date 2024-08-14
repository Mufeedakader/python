from datetime import datetime

# Initialize an empty list to store tasks
tasks = []

def add_task():
    """Add a new task."""
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD) or leave blank: ")
    task = {
        'description': description,
        'completed': False,
        'deadline': deadline
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
        return
    
    for i, task in enumerate(tasks):
        status = 'Completed' if task['completed'] else 'Pending'
        deadline = task['deadline'] if task['deadline'] else 'No deadline'
        print(f"{i + 1}. {task['description']} - {status} - Deadline: {deadline}")

def mark_task_complete():
    """Mark a task as completed."""
    view_tasks()
    if not tasks:
        return
    task_index = int(input("Enter the number of the task to mark as complete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    """Delete a task."""
    view_tasks()
    if not tasks:
        return
    task_index = int(input("Enter the number of the task to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the to-do list application."""
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
