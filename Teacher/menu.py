import os

import common_modules.global_menu as main_menu
from Teacher import assignment, student
from common_modules import global_variable


def show_assignment_detail(id):
    os.system('cls')
    assignment_id = int(id)
    assignment_detail = assignment.get_detail(assignment_id)

    if assignment_detail is not None:

        assignment_status = assignment.get_status(assignment_id)

        print(f"{assignment_detail['title']}")
        print()
        print(
            f"Batas waktu: {(assignment_detail['due_date'] if len(assignment_detail['due_date']) != 0 else 'Tidak ada')} ")

        print()

        print(f"Siswa yang sudah mengerjakan tugas ini: {'' if len(assignment_status) != 0 else '-'}")
        for index, student in enumerate(assignment_status):
            print(f"{index + 1}. {student['student_id']}")

        print()

        print("Petunjuk:")
        print("1. E untuk mengubah nama tugas")
        print("2. ED untuk mengubah batas waktu")
        print("3. - untuk menghapus tugas")
        print("4. B untuk kembali ke menu sebelumnya")

        selected_menu = input("Silakan pilih menu >> ").upper()
        match selected_menu:
            case "E":
                os.system('cls')
                _title = input("Masukkan judul tugas baru (kosongkan apabila ingin membatalkan) >> ")

                due_date = assignment_detail["due_date"]
                description = assignment_detail["description"]

                title = _title if len(_title) != 0 else assignment_detail["title"]

                assignment_update = assignment.update(
                    assignment_id,
                    {"title": title, "description": description, "due_date": due_date}
                )

                if assignment_update:
                    os.system('cls')
                    print("Judul berhasil diubah!")
                else:
                    os.system('cls')
                    print("Judul gagal diubah!")

            case "ED":
                os.system('cls')
                _due_date = input("Masukkan batas waktu baru (kosongkan apabila ingin membatalkan) >> ")

                title = assignment_detail["title"]
                description = assignment_detail["description"]

                due_date = _due_date if len(_due_date) != 0 else assignment_detail["due_date"]

                assignment_update = assignment.update(
                    assignment_id,
                    {"title": title, "description": description, "due_date": due_date}
                )

                if assignment_update:
                    os.system('cls')
                    print("Batas waktu tugas berhasil diubah!")
                else:
                    print("Batas waktu tugas gagal diubah!")
            case "-":
                delete_decision = input("Yakin ingin menghapus tugas ini? Status siswa yang mengerjakan tugas juga "
                                        "akan terhapus (y/n) >> ").upper()
                match delete_decision:
                    case "Y":
                        assignment_delete = assignment.delete(assignment_id)
                        if assignment_delete:
                            os.system('cls')
                            print("Tugas berhasil dihapus!")
                        else:
                            os.system('cls')
                            print("Tugas gagal dihapus!")
                    case "N":
                        os.system('cls')
                        print("Operasi dibatalkan")
                show_assignment_detail(id)
            case "B":
                show_assignment_manage_menu()
    else:
        print("Tugas tidak ditemukan!")


def show_assignment_manage_menu():
    os.system('cls')
    while True:
        assignments = assignment.get_all()
        if assignments['count'] != 0:
            print(f"Ada {assignments['count']} tugas:")

            for index, item in enumerate(assignments["assignments"]):
                print(f"{item['id']} {item['title']}")

            print()
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

        selected_menu = input("Silakan pilih menu >> ").upper()
        if selected_menu.lstrip("-").isdigit():
            if int(selected_menu) >= 0:
                show_assignment_detail(selected_menu)
            else:
                print("Silakan masukkan angka yang valid")
        else:
            match selected_menu:
                case "+":
                    os.system('cls')
                    assignment_title = input("Judul tugas: ")
                    assignment_description = input("Deskripsi tugas:")

                    while True:
                        has_due_date = input("Ingin menambah batas waktu (y/n): ").upper()
                        match has_due_date:
                            case "Y":
                                assignment_due_date = input("Batas waktu tugas (dd/mm/yyyy): ")
                                break
                            case "N":
                                assignment_due_date = None
                                os.system('cls')
                                break
                            case _:
                                print("Pilihan tidak ada")

                    create_assignment = assignment.create(
                        assignment_title,
                        assignment_description,
                        assignment_due_date
                    )

                    if create_assignment:
                        os.system('cls')
                        print("Tugas berhasil ditambahkan!")
                    else:
                        os.system('cls')
                        print("Tugas gagal ditambahkan!")

                case "B":
                    show_main_menu()


def show_student_detail(id):
    print()


def show_student_manage_menu():
    os.system('cls')
    while True:
        print("DAFTAR SISWA")
        print(student.get_students())

        print()
        print("Petunjuk:")
        print("1. Masukkan nomor siswa untuk melihat data siswa")
        print("2. + untuk menambahkan siswa")
        print("3. B untuk kembali ke menu sebelumnya")

        selected_menu = input("Silakan pilih menu >> ").upper()
        if selected_menu.lstrip("-").isdigit():
            if int(selected_menu) >= 0:
                show_student_detail(selected_menu)
            else:
                print("Silakan masukkan angka yang valid")
        else:
            match selected_menu:
                case "+":
                    os.system('cls')
                    student_name = input("Nama siswa: ")
                    student_id = input("NIM: ")

                    add_student = student.add(
                        student_name,
                        student_id
                    )

                    if add_student:
                        os.system('cls')
                        print("Siswa berhasil ditambahkan!")
                    else:
                        os.system('cls')
                        print("Siswa gagal ditambahkan!")

                case "-":
                    os.system('cls')
                    student_id = input('Masukkan NIM siswa yang ingin di hapus')
                    student.delete(student_id)
                case "B":
                    show_main_menu()


def show_main_menu():
    os.system('cls')
    while True:

        print("[1] Tampilkan daftar siswa")
        print("[2] Tampilkan daftar tugas")
        print("[3] Keluar dari akun")

        selected_menu = input("Silakan pilih menu >> ")
        match selected_menu:
            case "1":
                show_student_manage_menu()
                print()
            case "2":
                show_assignment_manage_menu()
            case "3":
                global_variable.session.clear()
                os.system('cls')
                main_menu.show_roles_menu()
