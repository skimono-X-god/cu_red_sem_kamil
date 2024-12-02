import json
import os
import csv

class Task:
    def __init__(self, id, title : str = None, description : str = None, done : bool = False, priority: str = None, due_date : str = None):
        if not title:
            raise ValueError("Заголовок задачи - обязательное поле")
        self.id = id
        self.title = title
        self.description = description if description else None
        self.done = done
        self.priority = priority
        self.due_date = due_date if due_date else None

    def to_dict(self):
        return dict(id = self.id, title = self.title, description = self.description, done = self.done, priority = self.priority, due_date = self.due_date)

    @staticmethod
    def from_dict(data : dict):
        return Task(data['id'], data['title'], data['description'], data['done'], data['priority'], data['due_date'])

    def __str__(self):
        return (f"Задача с ID: {self.id}, Заголовок: {self.title}, Описание: {self.description}, Статус: {self.done}, Приоритет: {self.priority}, Срок выполнения задачи: {self.due_date}")

    @staticmethod
    def load_tasks():
        if not os.path.exists('tasks.json'):
            return []
        with open('tasks.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Task.from_dict(task) for task in data]

    @staticmethod
    def save_tasks(tasks):
        with open('tasks.json', 'w', encoding='utf-8') as file:
            data = [task.to_dict() for task in tasks]
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def create_task(title : str, description: str = None, priority: str = None, done: bool = False, due_date: str = None):
        tasks = Task.load_tasks()
        task_id = 1
        for task in tasks:
            task_id = max(task_id, task.id + 1)
        new_task = Task(task_id, title, description, done, priority, due_date)
        tasks.append(new_task)
        Task.save_tasks(tasks)

    @staticmethod
    def show_tasks():
        tasks = Task.load_tasks()
        if len(tasks) == 0:
            print('Задач нет')
        else:
            for task in tasks:
                print(task)

    @staticmethod
    def mark_task_as_done(task_id: int):
        tasks = Task.load_tasks()
        for i, task in enumerate(tasks):
            if task.id == task_id:
                task.done = True
                Task.save_tasks(tasks)
                print(f'Задача с ID {task_id} успешно помечена как выполненная')
                return
        print(f'Задача с ID {task_id} не найдена')

    @staticmethod
    def edit_task(task_id: int, new_title: str = None, new_description: str = None, new_priority: str = None, new_done: bool = None, new_due_date: str = None):
        tasks = Task.load_tasks()
        for i, task in enumerate(tasks):
            if task.id == task_id:
                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description
                if new_priority:
                    task.priority = new_priority
                if new_done is not None:
                    task.done = new_done
                if new_due_date:
                    task.due_date = new_due_date
                Task.save_tasks(tasks)
                print(f'Задача с ID {task_id} успешно изменена')
                return
        print(f'Задача с ID {task_id} не найдена')

    @staticmethod
    def delete_task(task_id : int):
        tasks = Task.load_tasks()
        l1 = len(tasks)
        tasks = [task for task in tasks if task.id != task_id]
        l2 = len(tasks)
        Task.save_tasks(tasks)
        if l1 != l2:
            print(f'Задача с ID {task_id} успешно удалена')
        else:
            print(f'Задача с ID {task_id} не найдена')

    @staticmethod
    def export_tasks_to_csv(file_name):
        if not file_name:
            file_name = "tasks.csv"
        tasks = Task.load_tasks()
        with open(file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Title", "Description", "Done", "Priority", "Due Date"])
            for task in tasks:
                writer.writerow([task.id, task.title, task.description, task.done, task.priority, task.due_date])
        print(f"Задачи успешно экспортированы в {file_name}.")

    @staticmethod
    def import_tasks_from_csv(file_name):
        if not file_name:
            file_name = "tasks.csv"
        tasks = []
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                task_id = row['ID'] if row['ID'] else None
                task_title = row['Title'] if row['Title'] else None
                task_description = row['Description'] if row['Description'] else None
                task_done = None
                if row['Done'] == 'True':
                    task_done = True
                elif row['Done'] == 'False':
                    task_done = False
                task_priority = row['Priority'] if row['Priority'] else None
                task_due_date = row['Due Date'] if row['Due Date'] else None
                tasks.append(Task(int(task_id), task_title, task_description, task_done, task_priority, task_due_date))
            Task.save_tasks(tasks)
