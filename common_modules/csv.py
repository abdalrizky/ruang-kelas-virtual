import csv

import tabulate as table


# Fungsi untuk menampilkan file .csv
def show(path):
    with open(path) as csv_file:
        csv_obj = csv.reader(csv_file)
        print(table.tabulate(csv_obj, headers='firstrow'))


def read(path):
    data = []
    with open(path) as csv_file:
        csv_obj = csv.DictReader(csv_file)
        for row in csv_obj:
            data.append(row)
    return data

def write(path, data):
    with open(path, "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data)
