from common_modules import csv


# Fungsi untuk mendapatkan data lengkap tugas
def get_assignments(student_id):
    assignments = csv.read("database/assignments.csv")
    assignment_status = csv.read("database/assignment_status.csv")

    assignments_filtered_by_student_status = []

    for assignment in assignments:


        stat = None

        for status in assignment_status:
            # Jika assignment_id dan student_id cocok
            if status["assignment_id"] == assignment["id"] and status["student_id"] == str(student_id):
                # Tetapkan variabel status sama dengan status yang ada di assignment_status
                stat = status["status"]
                break

        # Gabungkan tugas yang telah difilter, ditambah satu field tambahan (status)
        assignments_filtered_by_student_status.append(
            {
                'id': assignment["id"],
                'title': assignment['title'],
                'description': assignment['description'],
                'due_date': assignment['due_date'],
                'status': stat
            }
        )
    return assignments_filtered_by_student_status


# Fungsi untuk mengambil detail penugasan
def get_detail(id):
    assignments = csv.read('database/assignments.csv')
    try:
        # Filter assignment berdasarkan id
        assignments_filtered = [assignment for assignment in assignments if assignment["id"] == str(id)]
        return assignments_filtered[0]
    except IndexError:
        return None


# Fungsi untuk mengerjakan tugas
def do(id, student_id):
    csv.write("database/assignment_status.csv", [
        student_id, id, "finish"
    ])
