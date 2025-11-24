# el menu de la app, el punto de entrada de la app

def main():
    print("\n--- Task Genie, your smart task manager ---")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

choice = input("choose an option: ")

match choice:
    case "1":
        pass
    case "2":
        pass
    case "3":
        pass
    case "4":
        pass
    case "5":
        pass
    case _:
        print("Not a valid option. Please choose another")
    

# Definir el punto de partida del programa
# si el nombre del fichero se corresponde con el de main, arranca la funcion main
if __name__ == "__main__":
    main()