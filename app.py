from time import sleep

todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    todos.append(title)
    pass

def print_list():
    global todos
    print ("\n \n  THINGS TO DO: \n")
    lengthy =len(todos)
    for i in range (0,lengthy):
      print(str(i+1)+")"+ " "+ todos[i] + "\n")
      sleep(0.4)
    pass

def delete_task(number_to_delete):
    global todos
    number_as_int = int(number_to_delete)
    number_as_int = number_as_int - 1
 #  deleted_item = int(todos[number_as_int])
    print("... deleting item" +" "+ str(number_as_int+1))
    del todos[number_as_int]
    sleep(0.6)
    print_list()
    pass

def save_todos():
    # your code here
    pass

    
def load_todos():
    # your code here
    pass

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")