from common_modules import csv


# Fungsi untuk membuat tugas baru
def create(title, description, due_date):
    # Ambil id di baris paling terakhir
    last_id = csv.get_last_row("database/assignments.csv")[0]

    # Jika id yang didapat adalah string id, tetapkan assignment_id sebagai 0
    if last_id == "id":
        assignment_id = 0
    else:
        assignment_id = int(last_id) + 1

    # Tulis data ke .csv
    csv.write(
        "database/assignments.csv",
        [assignment_id, str(title).title(), description, due_date]
    )
    return True


# Fungsi untuk mengambil status penugasan tiap Student
def get_status(id):
    assignment_status = csv.read('database/assignment_status.csv')

    # Filter status tugas berdasarkan assignment_id
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

    # Cari detail tugas berdasarkan id
    try:
        assignments_filtered = []
        for assignment in assignments:
            if assignment['id'] == str(id):
                assignments_filtered.append(assignment)

        return assignments_filtered[0]
    # Tangkap eror dan kembalikan nilai None
    except IndexError:
        return None


# Fungsi untuk mengubah rincian tugas
def update(id, new_data):
    # Edit baris di .csv berdasarkan id
    csv.edit_row(
        "database/assignments.csv",
        id,
        [id, new_data['title'], new_data['description'], new_data['due_date']]
    )
    return True


# Fungsi untuk menghapus tugas
def delete(id):
    # Hapus baris di .csv berdasarkan id
    csv.delete_row(
        "database/assignments.csv",
        id
    )
    return True
