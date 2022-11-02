from PyInquirer import prompt
import csv
import numpy as np
import pandas as pd


def create_user_matrix():
    with open('users.csv', 'r') as csv_file:
        reader = list(csv.reader(csv_file))
        L = []
        for row in reader:
            L.append(row[0])
        csv_file.close()
    size = len(L)
    print(size)
    m = np.zeros((size, size))
    df = pd.DataFrame(m, index=L, columns=L)
    return df


def show_status():
    df = create_user_matrix()

    return
