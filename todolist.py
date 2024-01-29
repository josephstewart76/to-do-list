class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the todo list.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed from the todo list.')
        else:
            print(f'Task "{task}" not found in the todo list.')

    def view_tasks(self):
        if self.tasks:
            print("Todo List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')
        else:
            print("Todo list is empty.")

# Example usage
if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Exiting the todo list program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

