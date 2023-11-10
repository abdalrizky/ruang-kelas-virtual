
from common_modules import csv



def get_students():
    student_data = csv.read('database/students.csv')
    for index, student in enumerate(student_data):
        print(f"{index} {student['NIM']} {student['Nama']}")

def show_students_as_table():
    csv.show('database/students.csv')

def update(id, new_data):
    csv.edit_row(
        "database/students.csv",
        id,
        [id, new_data['nim'], str(new_data['name']).upper()]
    )
    return True

def get_detail(id):
    students = csv.read('database/students.csv')
    try:
        assignments_filtered = []
        for student in students:
            if student['id'] == str(id):
                assignments_filtered.append(student)

        return assignments_filtered[0]
    except IndexError:
        return None



def add(student_name, student_nim):
    last_id = csv.get_last_item("database/students.csv")[0]
    if last_id == "id":
        student_id = 0
    else:
        student_id = int(last_id) + 1
    csv.write(
        "database/students.csv",
        [student_id, student_nim, str(student_name).upper()]
    )
    return True

def delete(id):
    csv.delete_row(
        "database/students.csv",
        id
    )
    return True
