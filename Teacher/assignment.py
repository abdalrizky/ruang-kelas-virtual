from common_modules import csv


# Fungsi untuk membuat tugas baru
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


# Fungsi untuk mengambil status penugasan tiap Student
def get_status(id):
    assignment_status = csv.read('database/assignment_status.csv')
    finished_students = [student for student in assignment_status if student["assignment_id"] == str(id)]
    return finished_students


# Fungsi untuk menampilkan semua tugas
def get_all():
    assignments = csv.read('database/assignments.csv')
    return {
        "count": len(assignments),
        "assignments": assignments
    }


# Fungsi untuk mengambil detail penugasan
def get_detail(id):
    assignments = csv.read('database/assignments.csv')
    try:
        assignments_filtered = []
        for assignment in assignments:
            if assignment['id'] == str(id):
                assignments_filtered.append(assignment)

        return assignments_filtered[0]
    except IndexError:
        return None


# Fungsi untuk mengubah rincian tugas
def update(id, new_data):
    csv.edit_row(
        "database/assignments.csv",
        id,
        [id, new_data['title'], new_data['description'], new_data['due_date']]
    )
    return True


# Fungsi untuk menghapus tugas
def delete(id):
    csv.delete_row(
        "database/assignments.csv",
        id
    )
    return True
