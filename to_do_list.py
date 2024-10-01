from datetime import datetime
from tabulate import tabulate # type: ignore
import csv

""" TO DO LIST """

""" Funcionalites 
    - Add items
    - Edit items
    - Remove items
    - Mark as finished
    - Priority activites
    - Save in a CSV file """

# Date right now
date = datetime.now()
date_now = (date.strftime("%y-%m-%d %H:%M:%S"))


to_do = []
csv_file = "data/to_do_list.csv"
backup = ...

def main():

    # Open csv file
    open_file()

    print("\n+++ TO DO LIST +++")
    
    while True:

        option = menu()
         
        if option == "1":
            show_items(to_do)
        elif option == "2":
            add_items(to_do)
        elif option == "3":
            edit_item(to_do)
        elif option == "4":
            remove_item(to_do)
        elif option == "5":
            save_task_list(to_do)
            print("\nHave a good day!\n")
            break
    

def open_file():
    with open(csv_file, "r") as list_file:
        reader = csv.DictReader(list_file)
        for row in reader:
            to_do.append(row)            


def menu():
    print("""\n[1] - SHOW TASKS
[2] - Add item
[3] - Edit item
[4] - Remove item
[5] - Exit \n""")
    
    return input("What do you want to do? ")


def show_items(tasks):
    print(tabulate(tasks, headers="keys", tablefmt="grid"))


def add_items(tasks):
    item = input("New task: ")
    time = input("Time: ")
    tasks.append({"task": item, "time": time, "created": date_now})
    while True:
        answer = input("Do you wanna add a another task [Y/N]: ").upper()
        if answer == "Y":
            date = datetime.now()
            hour_now = (date.strftime("%y-%m-%d %H:%M:%S"))
            tasks.append({"task": input("New task: "), "time": input("Time: "), "created": hour_now})
        elif answer == "N":
            break
        else:
            pass


def edit_item(my_list):
    list_size = int(len(my_list))

    print("\nWhich item do you want to edit?\n")

    # Show list.
    for i in range(list_size):
        print(f"{i+1} - {my_list[i]['task']} - {my_list[i]['time']}")

    # Item that user to want to edit.
    item_number = int(input("Item number: "))
    if item_number <= list_size:
        for j in range(list_size):
            if item_number == j+1:
                my_list[j] = {"task": input("New name: "), "time": input("Time: "), "created": date_now}

    
def remove_item(my_list):
    list_size = int(len(my_list))
    print("\nWhich item do you want to remove?\n")

    # Show list.
    for i in range(list_size):
        print(f"{i+1} - {my_list[i]['task']} - {my_list[i]['time']}")

    # Item that user to want to remove.
    item_number = int(input("\nItem number: "))
    if item_number <= list_size:
        for j in range(list_size):
            if item_number == j+1:
                my_list.pop(j)


def save_task_list(my_list):

    list_size = int(len(my_list))

    # Create file
    with open(csv_file, "w") as list_file:
        writer = csv.writer(list_file)
        writer.writerow(["task", "time", "created"])

    for k in range(list_size):
        task = my_list[k]["task"]
        time = my_list[k]["time"]
        create = my_list[k]["created"]
        # write each row in the csv file
        with open(csv_file, "a") as list_file:
            writer = csv.DictWriter(list_file, fieldnames=["task", "time", "created"])
            writer.writerow({"task": task, "time": time, "created": create})

    # Create a PDF


    

if __name__ == "__main__":
    main()

