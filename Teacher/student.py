from common_modules import csv


# Fungsi untuk menunjukkan data siswa dalam bentuk tabel
def show_as_table():
    csv.show('database/students.csv')


# Fungsi untuk mengupdate data siswa
def update(id, new_data):
    # Edit baris di .csv berdasarkan id
    csv.edit_row(
        "database/students.csv",
        id,
        [id, new_data['nim'], str(new_data['name']).upper()]
    )
    return True


# Fungsi mengambil detail data siswa
def get_detail(id):
    students = csv.read('database/students.csv')

    # Cari detail siswa berdasarkan id
    try:
        assignments_filtered = []
        for student in students:
            if student['id'] == str(id):
                assignments_filtered.append(student)

        return assignments_filtered[0]
    # Tangkap eror dan kembalikan nilai None
    except IndexError:
        return None


# Fungsi untuk menambahkan siswa ke dalam .csv
def add(student_name, student_nim):
    # Ambil id di baris paling terakhir
    last_id = csv.get_last_row("database/students.csv")[0]

    # Jika id yang didapat adalah string id, tetapkan last_id sebagai 0
    if last_id == "id":
        student_id = 0
    else:
        student_id = int(last_id) + 1

    # Tulis data ke .csv
    csv.write(
        "database/students.csv",
        [student_id, student_nim, str(student_name).upper()]
    )
    return True


# Fungsi untuk menghapus data siswa
def delete(id):
    # Hapus baris di .csv berdasarkan id
    csv.delete_row(
        "database/students.csv",
        id
    )
    return True
