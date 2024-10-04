from datetime import datetime
from tabulate import tabulate # type: ignore
import csv
from fpdf import FPDF


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
    pdf(to_do)



def pdf(my_list):
    class PDF(FPDF):
        def __init__(self):
            super().__init__()

        def title_pdf(self, title):
            # Title
            self.set_font("Arial", "", 50)
            self.set_text_color(0, 0, 128)
            self.cell(197, 60, f"{title}", align="C")
            self.ln(30)

        def header_list(self, text):
            self.set_font("Helvetica", "B", 24)
            self.set_text_color(255, 0, 0)
            self.cell(40)
            self.cell(150, 50, f"{text}", align="")
            self.ln(18)

        def line_1(self, text):
            self.set_font("Helvetica", "B", 20)
            self.set_text_color(0, 0, 0)
            self.cell(30)
            self.cell(150, 50, f"{text}", align="")

        def footer(self):
            self.set_font("helvetica", "I", 10)
            self.set_text_color(0, 0, 0)
            self.cell(197, 15, f"Last Update {date_now}", align="C")
    

        def break_line(self, line):
            self.ln(line)

    # Size of the list
    list_size = int(len(my_list))

    pdf = PDF()
    pdf.add_page()

    pdf.title_pdf("+++ To DO List +++")

    pdf.header_list("Tasks")
    
    for i in range(list_size):
        pdf.line_1(f" - {my_list[i]['task']} at {my_list[i]['time']} -")
        #pdf.line_2(tabulate(f"{my_list[i]['created']}"))
        pdf.break_line(10)
    
    pdf.break_line(30)
    pdf.footer()
    
    pdf.output("outputs/test.pdf")

    print("\nPDF created successfully")
    print(date_now)



if __name__ == "__main__":
    main()

