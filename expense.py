from PyInquirer import prompt
import csv
from user import read_users, add_user


expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "input",
        "name": "spender",
        "message": "New Expense - Spender: ",
    },

]


def add_stop_option():
    L = read_users()
    L.append("Stop")
    return L


users = [
    {
        'type': 'rawlist',
        'name': 'users',
        'message': 'Select users or select Stop when you are done : ',
        'choices': add_stop_option(),
    },
]


def export_expense(infos):
    with open('expense_report.csv', 'a') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.DictWriter(f, infos.keys())
        w.writeheader()
        w.writerow(infos)


def new_expense(*args):
    infos = prompt(expense_questions)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    tmp = ""
    List_of_users_involved = []
    while tmp != "Stop":
        user = prompt(users)
        tmp = user["users"]
        if tmp == "Stop":
            break
        List_of_users_involved.append(tmp)
    add_user(infos["spender"])
    List_of_users_involved.append(infos["spender"])

    cost_of_each = int(infos["amount"]) // (len(List_of_users_involved))
    print("Each people need to refund : " +
          str(cost_of_each) + " to " + infos["spender"])

    infos["people_involved"] = List_of_users_involved
    export_expense(infos)
    return True
