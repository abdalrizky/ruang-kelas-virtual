
from common_modules import csv



def get_students():
    student_data = csv.read('database/students.csv')
    for index, student in enumerate(student_data):
        print(f"{index}. {student}")



def add(student_name, student_id):
    csv.write(
        "database/students.csv",
        [student_id, str(student_name).capitalize(), "A23"]
    )
    return True

def delete(student_id):
    students = csv.read('database/students.csv')
    for student in students:
        if student['NIM'] == student_id:
            # deleted
            print()
    # csv.write('database/students.csv', )
