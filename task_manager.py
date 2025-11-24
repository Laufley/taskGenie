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

    def __init__(self):
        self._tasks = [] #indico k es un atributo "privado" on el underscore. Es solo para marcar a otros devs k no lo accedan directamente
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self._tasks.append(task)
        self.next_id += 1
        print(f"Added task: {description}")
    
    def list_tasks(self):
        pass

    def complete_task(self, id):
        pass

    def delete_task(self, id):
        pass