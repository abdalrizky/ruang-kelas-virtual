import common_modules.global_menu as main_menu
from Teacher import assignment
from common_modules import csv, global_variable


def show_assignment_manage_menu():
    while True:
        # csv.show("database/assignment.csv")
        assignments = assignment.show_all()
        if assignments['count'] != 0:
            print(f"Ada {assignments['count']} tugas")

            for index, item in enumerate(assignments["assignments"]):
                print(f"{index + 1}. {item['title']}")

            print("Petunjuk:")
            print("1. Masukkan nomor tugas untuk melihat rincian tugas")
            print("2. + untuk menambahkan tugas")
            print("3. B untuk kembali ke menu sebelumnya")
        else:
            print("Belum ada tugas yang dibuat")
            print()
            print("Petunjuk:")
            print("1. + untuk menambahkan tugas")
            print("2. B untuk kembali ke menu sebelumnya")

        selected_menu = input("Silakan pilih menu >> ")
        if selected_menu.lstrip("-").isdigit():
            print() # Tampilkan detail tugas
        else:
            match selected_menu:
                case "+":
                    assignment_title = input("Judul tugas: ")
                    assignment_description = input("Deskripsi tugas:")
                    assignment_due_date = input("Batas waktu tugas (dd/mm/yyyy): ")
                    create_assignment = assignment.create(
                        assignment_title,
                        assignment_description,
                        assignment_due_date
                    )

                    if create_assignment:
                        print("Tugas berhasil ditambahkan!")
                    else:
                        print("Tugas gagal ditambahkan!")

                case "B":
                    show_main_menu()



def show_main_menu():
    while True:

        print("[1] Tampilkan daftar siswa")
        print("[2] Tampilkan daftar tugas")
        print("[3] Keluar dari akun")

        selected_menu = input("Silakan pilih menu >> ")
        match selected_menu:
            case "1":
                csv.show('database/students.csv')
            case "2":

                show_assignment_manage_menu()
            case "3":
                global_variable.session.clear()
                main_menu.show_roles_menu()
