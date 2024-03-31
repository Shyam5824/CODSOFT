print("\t TO-DO LIST")
tasks = []
def add_task(task):
    tasks.append(task)
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found!")
def display_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")
def update_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = new_task
    else:
        print("Invalid task index!")
def main():
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Update Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            index = int(input("Enter task index to update: "))
            new_task = input("Enter new task: ")
            update_task(index, new_task)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")
if __name__=="__main__":
    main()
    
