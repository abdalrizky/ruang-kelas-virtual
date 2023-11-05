import csv


# Fungsi untuk mencari NIM apakah ada pada data csv
def search_nim(nim):
    reader = csv.reader(open('database/students.csv'))
    for i in reader:
        if nim in i:
            return {
                "nim": i[0],
                "name": i[1],
                "class": i[2]
            }
    return None
