# el menu de la app, el punto de entrada de la app pk tiene la funcion main()
from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
    print("\n--- Task Genie, your smart task manager ---")
    print("1. Add task")
    print("2. Add complex task with AI")
    print("3. List tasks")
    print("4. Complete task")
    print("5. Delete task")
    print("6. Exit")

def main():

    manager = TaskManager()

    while True:

        print_menu()

        try: 
            choice = int(input("choose an option: "))

            match choice:
                case 1:
                    description = input("Describe the task: ")
                    manager.add_task(description)
                case 2:
                    description = input("Describe the complex task: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("Error:"):
                            manager.add_task(subtask)
                        else:
                            print(subtask)
                            break
                case 3:
                    manager.list_tasks()
                case 4:
                    id = int(input("ID of the task to complete: "))
                    manager.mark_complete_task(id)
                case 5:
                    id = int(input("ID of the task to delete: "))
                    manager.delete_task(id)
                case 6:
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