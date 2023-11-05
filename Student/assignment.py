# Fungsi untuk mendapatkan data lengkap tugas
def get_assignments():
    return {
        "count": 1,
        "assignments": [
            {
                "status": "finish",
                "name": "Tugas 1",
                "grade": None
            }
        ]
    }


# Fungsi untuk mengerjakan tugas
def do(id):
    print()
