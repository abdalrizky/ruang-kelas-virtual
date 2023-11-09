# Fungsi untuk membuat tugas baru
from common_modules import csv


def create(title, description, due_date):
    last_id = csv.get_last_item("database/assignments.csv")[0]
    if last_id == "id":
        assignment_id = 0
    else:
        assignment_id = int(last_id) + 1
    csv.write(
        "database/assignments.csv",
        [assignment_id, title, description, due_date]
    )
    return True


def get_status(id):
    assignment_status = csv.read('database/assignment_status.csv')
    return assignment_status


# Fungsi untuk menampilkan semua tugas
def get_all():
    assignments = csv.read('database/assignments.csv')
    return {
        "count": len(assignments),
        "assignments": assignments
    }


def get_detail(id):
    assignments = csv.read('database/assignments.csv')
    try:
        return [assignment for assignment in assignments if assignment["id"] == str(id)]
    except IndexError:
        return None


# Fungsi untuk mengubah rincian tugas
def update(id, new_data):
    print("Perbarui Tugas")


# Fungsi untuk menghapus tugas
def delete(id):
    print("Tugas dihapus")
