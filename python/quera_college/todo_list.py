import csv
import os
import sys


class Task:
    def __init__(self, title, priority='Medium', done=False):
        self.title = title
        self.priority = priority
        self.done = done


class TodoList:
    def __init__(self):
        self.file_name = 'todo.csv'
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name) as file:
                reader = csv.reader(file)

                for line in reader:
                    title, priority, done = line
                    self.tasks.append(
                        Task(title.strip(), priority.strip(), bool(int(done))))

    def save_tasks(self):
        with open(self.file_name, mode='w') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task.title, task.priority, int(task.done)])

    def find_task(self, title):
        task = next((task for task in self.tasks if task.title == title), None)
        if not task:
            print('Invalid title.')
        return task

    def update_task(self, title, field, edit):
        task = self.find_task(title)
        if task:
            setattr(task, field, edit)
            self.save_tasks()
            print(f'Task "{title}" updated successfully.')

    def delete_task(self, title):
        task = self.find_task(title)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f'Task "{title}" deleted successfully.')

    def clear_list(self):
        self.tasks.clear()
        self.save_tasks()
        print('To-do list cleared successfully.')

    def create_task(self, title, priority='Medium', done=False):
        task = Task(title, priority, done)
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{title}" created successfully.')

    def get_task(self, title):
        task = self.find_task(title)
        if task:
            print("{:<15} {:<10} {:<10}".format('Title', 'Priority', 'Done'))
            print("{:<15} {:<10} {:<10}".format(
                task.title, task.priority, task.done))

    def list_tasks(self):
        if len(self.tasks) == 0:
            print('No tasks found.')
        else:
            print('Task List:')
            print("{:<6} {:<15} {:<10} {:<10}".format(
                'Index', 'Title', 'Priority', 'Done'))
            for index, task in enumerate(self.tasks, start=1):
                print("{:<6} {:<15} {:<10} {:<10}".format(
                    index, task.title, task.priority, task.done))


def main():
    todo_list = TodoList()
    invalid_msg = 'Invalid command.'
    if len(sys.argv) < 2:
        print(invalid_msg)
        return

    command = sys.argv[1]

    if command == 'list':
        todo_list.list_tasks()
    elif command == 'create':
        args = sys.argv[2:]
        if len(args) < 1:
            print(invalid_msg)
        else:
            todo_list.create_task(args[0], args[1] if len(
                args) >= 2 else 'Medium', args[2] if len(args) == 3 else 0)
    elif command == 'update':
        args = sys.argv[2:]
        if len(args) < 3:
            print(invalid_msg)
        else:
            todo_list.update_task(args[0], args[1], args[2])
    elif command == 'delete':
        args = sys.argv[2:]
        if len(args) == 0:
            print(invalid_msg)
        else:
            todo_list.delete_task(args[0])
    elif command == 'clear':
        todo_list.clear_list()
    elif command == 'search':
        args = sys.argv[2:]
        if len(args) == 0:
            print(invalid_msg)
        else:
            todo_list.get_task(args[0])
    else:
        print(invalid_msg)


if __name__ == "__main__":
    main()
