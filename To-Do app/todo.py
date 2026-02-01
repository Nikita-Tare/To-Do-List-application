def display_menu():
    print("\nTo-Do list Application")
    print("1. view task")
    print("2. Add task")
    print("3.Delete Task")
    print("4.Exit")

def view_task(tasks):
    if not tasks:
        print("No Task Available")
    else:
        print('/n your To-Do list:')
        index=1
        for task in tasks:
            print(f"{index}.{task}")
            index += 1 
            
            
def Add_task(tasks):
    task=input("Enter your task to add: ")
    tasks.append(task)
    print(f"Task added successfully")

def Delete_task(tasks):
    view_task(tasks)
    try:
        task_number=int(input("enter the number to delete: "))
        if 1 <= task_number <= len(tasks):
            remove_task=tasks.pop(task_number -1 )
            print(f"task deleted successfully.")
        else:
            print("invalid task number. please try again")
    except ValueError:
        print("Invalid input. please enter a valid task number. ")


def to_do_list_app():
    tasks=[]
    while True:
        display_menu()
        choice=input("Enter your choice (1-4):")
        if choice=='1':
            view_task(tasks)
        elif choice=='2':
            Add_task(tasks)
        elif choice=='3':
            Delete_task(tasks)
        elif choice=='4':
            print("Exiting the application Have a Nice Day !!!")
            break
        else:
            print("invalid choice please check the ennterd number")

to_do_list_app()
    