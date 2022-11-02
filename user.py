from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "Name",
        "message": "Name: ",
    },
]


def export_user(infos):
    with open('user_report.csv', 'a') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.writer(f)
        for key, value in infos.items():
            w.writerow([key, value])
        f.close()


def read_users():
    with open('user_report.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        L = []
        for row in reader:
            L.append(row[1])
        csv_file.close()
    return L


def add_user():
    infos = prompt(user_questions)
    export_user(infos)

    print("User Added !")
    # This function should create a new user, asking for its name
    return
