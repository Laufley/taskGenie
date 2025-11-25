import json

class Task:

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed


    #__str__: metodo magico/dunder method k Py usa para decidir k texto mostrar cuando convertimos un objeto to str. Por ejemplo, en print stattements.
    # Lo voy a re-definit para k muestre unos campos concretos
    def __str__(self):
        status =  "✔" if self.completed else " "
        return f"[{status} #{self.id}: {self.description}]"


# Clase para gestionar la lista de tareas. Se inicializa vacia.
class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = [] #indico k es un atributo "privado" on el underscore. Es solo para marcar a otros devs k no lo accedan directamente
        self.next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self.next_id, description)
        self._tasks.append(task)
        self.next_id += 1
        print(f"Added task: {description}")
        self.save_tasks()
    
    def list_tasks(self):
        if not self._tasks:
            print("There are no pending tasks")
        else:
            for task in self._tasks:
                print(task)
            
    def mark_complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Task marked as completed: {task}")
                self.save_tasks()
                return
            else:
                print(f"Task not found: #{id}")



    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Task deleted: {task}")
                self.save_tasks()
                return
            else:
                print(f"Task not found: #{id}")

    def load_tasks(self):
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item["completed"]) for item in data]
                if self._tasks:
                    self.next_id = self._tasks[-1].id + 1
                else:
                    self.next_id = 1

        except FileNotFoundError:
            self._tasks = []


    def save_tasks(self):
        with open(self.FILENAME, "w") as file:
            json.dump([{"id": task.id, "description": task.description, "completed": task.completed} for task in self._tasks], file, indent = 4)
        

    
