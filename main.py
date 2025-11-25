# el menu de la app, el punto de entrada de la app pk tiene la funcion main()
from task_manager import TaskManager

def print_menu():
    print("\n--- Task Genie, your smart task manager ---")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

def main():

    manager = TaskManager()

    while True:

        print_menu()

        try: 
            choice = int(input("choose an option: "))

            match choice:
                case 1:
                    description = input("Describe la tarea: ")
                    manager.add_task(description)
                case 2:
                    manager.list_tasks()
                case 3:
                    id = int(input("ID of the task to complete: "))
                    manager.mark_complete_task(id)
                case 4:
                    id = int(input("ID of the task to delete: "))
                    manager.delete_task(id)
                case 5:
                    print("Leaving...")
                    break
                case _:
                    print("Not a valid option. Please choose another")
        except ValueError:
             print("Not a valid option. Option must be a number. Please choose another")
    

# Definir el punto de partida del programa
# Only run main() if file is executed directly. Not if it´s imported from another file
if __name__ == "__main__":
    main()