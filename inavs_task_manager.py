import csv
import json
import datetime
from time import sleep

def show_tasks(a):
    with open('task.json', 'r', encoding='utf-8') as f:
        data_task = json.load(f)
        for task in data_task:
            if a == "1":
                if task['Status'] != "Deleted":
                    print(f"""id{task['ID']}  {task['Title']}. 
     {task['Description']}.
     {task['Create date']} - {task['Due date']}.
""")
            if a == "9":
                if task['Status'] == "Deleted":
                    print(f"""id{task['ID']}  | {task['Title']}. 
     {task['Description']}.
     {task['Create date']} - {task['Due date']}.
                    """)
            if a == "7":
                print(f"""id{task['ID']}  {task['Title']}. 
     {task['Description']}.
     {task['Create date']} - {task['Due date']}.
""")




def id_number():
    try:
        with open("task.json", "r") as id_file:
            id_data = json.load(id_file)
            for i in id_data:
                id_num = i["ID"]
            id_num +=1
        return id_num
    except:
        return 1



def add_task():
    try:
        id_num = id_number()
        title_name = input("Ent3r task title: ").strip()
        description_text = input("Ent3r task description: ").strip()
        task_status = "In progress"
        task_create_date = datetime.datetime.now()
        task_days_due = int(input("Task due(in days): ").strip() )
        task_due_date = task_create_date + datetime.timedelta(days=task_days_due)
        my_new_task = {"ID":id_num, "Title":title_name, "Description":description_text, "Status":task_status, "Create date":task_create_date.strftime("%d-%m-%Y"), "Due date" : task_due_date.strftime("%d-%m-%Y")}

        with open("task.json", "r") as fileread:
            my_tasks_opened = json.load(fileread)
            my_tasks_opened.append(my_new_task)
        with open('task.json', 'w', encoding='utf-8') as filewrite:
            json.dump(my_tasks_opened, filewrite, ensure_ascii=False, indent=4)
    except:
        print("""
DUE IN QUANTITY OF DAYS!!!""")
    print("Create DONE")


def delete_task():
    show_tasks("1")
    try:
        del_id = input("Enter ID of task to delete: ")
        with open("task.json", "r", encoding='utf-8') as fileread:
            my_tasks = json.load(fileread)
            if int(del_id) > len(my_tasks):
                print("ID not found")
            for i in my_tasks:
                if i["ID"] == int(del_id):
                    i["Status"] = "Deleted"

        with open('task.json', 'w', encoding='utf-8') as filewriter:
            json.dump(my_tasks, filewriter, ensure_ascii=False, indent=4)
    except:
        print(""" 
WRONG ID!!! 
        """)
    print("DELETE DONE")

def complete_task():
    show_tasks("1")
    del_id = input("Enter ID of task you complete: ")
    with open("task.json", "r", encoding='utf-8') as fileread:
        my_tasks = json.load(fileread)
        for i in my_tasks:
            if i["ID"] == int(del_id):
                i["Status"] = "Completed"
    with open('task.json', 'w', encoding='utf-8') as filewriter:
        json.dump(my_tasks, filewriter, ensure_ascii=False, indent=4)
    print("DONE")


def export_csv():
    with open("task.json", "r", encoding='utf-8') as filereader:
        data = json.load(filereader)

    with open('task.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data[0].keys())
        for i in data:
            writer.writerow(i.values())
    print("CSV DONE")

def task_edit():
    show_tasks("7")
    edit_id = input("Enter ID of task to edit: ").strip()
    edit_title = int(input("""   What you wanna edit?
  Press 1 to edit Title
  Press 2 to edit Description
  Press 3 to edit Due date
""").strip())
    with open("task.json", "r", encoding='utf-8') as fileread:
        data = json.load(fileread)
        for i in data:
            if i["ID"] == int(edit_id):
                if(edit_title == 1):
                    i["Title"] = input("Enter new title: ").strip()
                elif(edit_title == 2):
                    i["Description"] = input("Enter new description: ").strip()
                elif(edit_title == 3):
                    i["Due date"] = input("Enter new due date: ").strip()
    with open("task.json", "w", encoding='utf-8') as filewriter:
        json.dump(data, filewriter, ensure_ascii=False, indent=4)
    print("DONE")


def menu():
    a = "@inavinavov"
    while a != "q":
        a = input("""
        Press 1 to show your tasks.
        Press 2 to add a new task.
        Press 3 to delete the task.
        Press 4 to mark te completed tasks.
        Press 5 to edit any task.
        Press 7 to show all tasks(deleted + completed + in progress).
        press 8 to export csv.
        Press 9 to show deleted tasks
        press q to quit.

        """).strip()
        if a == "1":
            show_tasks(a)
        elif a == "2":
            add_task()
        elif a == "3":
            delete_task()
        elif a == "9":
            show_tasks(a)
        elif a == "4":
            complete_task()
        elif a == "8":
            export_csv()
        elif a == "5":
            task_edit()
        elif a == "7":
            show_tasks(a)
        elif a == "6":
            print("Самый умный?")
        else:
            print("Unknown command")

my_tasks = []


try:
    with open("task.json", "r") as file:
        data = json.load(file)
    print("Hello, User!")
    show_tasks("1")

except :
    print("""You have not added any tasks!
      OK let's go!""")
    sleep(1)
    title = input("Ent3r your first task title: ").strip()
    description = input("Ent3r task description: ").strip()
    status = "In progress"
    create_date = datetime.datetime.now()
    try:
        days_due = int(input("Task due(in days): ").strip())
    except:
        print("Due must be in days quantity! Due = 0")
        days_due = 0

    due_date = create_date + datetime.timedelta(days=days_due)
    my_task = {"ID": 1, "Title": title, "Description": description, "Status": status,
               "Create date": create_date.strftime("%d-%m-%Y"), "Due date": due_date.strftime("%d-%m-%Y")}
    my_tasks.append(my_task)
    with open('task.json', 'w', encoding='utf-8') as file:
        json.dump(my_tasks, file, ensure_ascii=False, indent=4)

menu()
