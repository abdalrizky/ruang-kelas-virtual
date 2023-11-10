import csv

from prettytable import from_csv


# Fungsi untuk menampilkan file .csv
def show(path):
    with open(path) as csv_file:
        target_table = from_csv(csv_file)
        print(target_table)


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


def edit_row(path, index, new_data):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        last_data = list(csv_reader)

    last_data[index + 1] = new_data
    with open(path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(last_data)


def delete_row(path, index):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        last_data = list(csv_reader)

    del last_data[index]
    with open(path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(last_data)


def get_last_item(path):
    rows = []

    with open(path) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(row)

    if len(rows) > 0:
        last_row = rows[-1]
        return last_row
