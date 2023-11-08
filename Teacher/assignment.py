# Fungsi untuk membuat tugas baru
from common_modules import csv


def create():
    print()


# Fungsi untuk menampilkan semua tugas
def show_all():
    assignments = csv.read('database/assignments.csv')
    return {
        "count": len(assignments),
        "assignments": assignments
    }


# Fungsi untuk mengubah rincian tugas
def update(id, new_data):
    print("Perbarui Tugas")


# Fungsi untuk menghapus tugas
def delete(id):
    print("Tugas dihapus")
