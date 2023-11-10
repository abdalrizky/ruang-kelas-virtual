from common_modules import csv


# Fungsi untuk mendapatkan data lengkap tugas
def get_assignments(student_id):
    assignments = csv.read("database/assignments.csv")
    assignments_filtered_by_student_status = []
    for assignment in assignments:
        assignments_filtered_by_student_status.append(assignment)
    return assignments_filtered_by_student_status



def get_detail(id):
    assignments = csv.read('database/assignments.csv')
    try:
        assignments_filtered = [assignment for assignment in assignments if assignment["id"] == str(id)]
        return assignments_filtered[0]
    except IndexError:
        return None

# Fungsi untuk mengerjakan tugas
def do(id, student_id):
    csv.write("database/assignment_status.csv", [
        student_id, id, "finish"
    ])

def get_status(id, student_id):
    # assignment_status = csv.read("database/assignment_status.csv")
    # assignment_filtered_by_student_id = [assignment for assignment in assignment_status if assignment["assignment_id"] == str(id) and assignment["student_id"] == str(student_id)]
    # return assignment_filtered_by_student_id

    assignments = get_assignments()
    print(assignments)

def compare_status():
    assignments = csv.read("database/assignments.csv")
    assignments_status = csv.read("")