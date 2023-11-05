import csv
import tabulate as table


# Fungsi untuk menampilkan file .csv
def show(path):
    with open(path) as csv_file:
        csv_obj = csv.reader(csv_file)
        print(table.tabulate(csv_obj, headers='firstrow'))
