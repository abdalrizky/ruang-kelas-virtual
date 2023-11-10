import csv

from prettytable import from_csv


# Fungsi untuk menampilkan file .csv
def show(path):
    with open(path) as csv_file:
        target_table = from_csv(csv_file)
        print(target_table)

# Fungsi untuk membaca file .csv menjadi dictionary
def read(path):
    data = []
    with open(path) as csv_file:
        csv_obj = csv.DictReader(csv_file)
        for row in csv_obj:
            data.append(row)
    return data

# Fungsi untuk mengwrite ke .csv
def write(path, data):
    with open(path, "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data)

# Fungsi untuk mengedit data dalam .csv
def edit_row(path, index, new_data):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        last_data = list(csv_reader)

    last_data[index + 1] = new_data
    with open(path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(last_data)

# Fungsi untuk menghapus data dalam .csv
def delete_row(path, index):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        last_data = list(csv_reader)

    del last_data[index]
    with open(path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(last_data)

# Fungsi untuk mengambil data terakhir dalam .csv
def get_last_item(path):
    rows = []

    with open(path) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(row)

    if len(rows) > 0:
        last_row = rows[-1]
        return last_row
