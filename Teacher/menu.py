import os
from datetime import datetime

from prettytable import PrettyTable

import common_modules.global_menu as main_menu
from Teacher import assignment, student
from common_modules import global_variable


# Fungsi untuk menunjukkan menu management penugasan bagi Teacher
def show_assignment_detail(id):
    os.system('cls')

    assignment_id = int(id)
    assignment_detail = assignment.get_detail(assignment_id)

    if assignment_detail is not None:

        assignment_status = assignment.get_status(assignment_id)

        print(assignment_detail['title'])
        print()
        print("Deskripsi:")
        print(assignment_detail['description'])
        print()
        print(
            f"Batas waktu: {(assignment_detail['due_date'] if len(assignment_detail['due_date']) != 0 else 'Tidak ada')} ")

        print()

        print(f"Siswa yang sudah mengerjakan tugas ini: {'' if len(assignment_status) != 0 else '-'}")
        for index, student in enumerate(assignment_status):
            print(f"{index + 1}. {student['student_id']}")

        print()

        print("Petunjuk:")
        print("[1] Ubah nama tugas")
        print("[2] Ubah deskripsi tugas")
        print("[3] Ubah batas waktu")
        print("[4] Hapus tugas")
        print("[5] Kembali ke menu sebelumnya")

        selected_menu = input("Silakan pilih menu >> ").upper()
        match selected_menu:
            case "1":
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
            case "2":
                os.system('cls')
                _description = input("Masukkan deskripsi tugas baru (kosongkan apabila ingin membatalkan) >> ")

                due_date = assignment_detail["due_date"]
                title = assignment_detail["title"]

                description = _description if len(_description) != 0 else assignment_detail["description"]

                assignment_update = assignment.update(
                    assignment_id,
                    {"title": title, "description": description, "due_date": due_date}
                )

                if assignment_update:
                    os.system('cls')
                    print("Deskripsi tugas berhasil diubah!")

            case "3":
                os.system('cls')
                while True:
                    _due_date = input("Masukkan batas waktu baru dd-mm-yyyy hh.mm (kosongkan apabila ingin "
                                      "membatalkan) >> ")
                    try:
                        if len(_due_date) != 0:
                            _due_date = datetime.strptime(_due_date, "%d-%m-%Y %H.%M")
                        break
                    except ValueError:
                        print("Silakan masukkan batas waktu sesuai format")

                title = assignment_detail["title"]
                description = assignment_detail["description"]

                due_date = _due_date if len(str(_due_date)) != 0 else assignment_detail["due_date"]

                assignment_update = assignment.update(
                    assignment_id,
                    {"title": title, "description": description, "due_date": due_date}
                )

                if assignment_update:
                    os.system('cls')
                    print("Batas waktu tugas berhasil diubah!")

            case "4":
                delete_decision = input("Yakin ingin menghapus tugas ini? (y/n) >> ").upper()
                match delete_decision:
                    case "Y":
                        assignment_delete = assignment.delete(assignment_id)
                        if assignment_delete:
                            os.system('cls')
                            print("Tugas berhasil dihapus!")
                    case "N":
                        os.system('cls')
                        print("Operasi dibatalkan")
                show_assignment_detail(id)
            case "5":
                show_assignment_manage_menu()

    else:
        print("Tugas tidak ditemukan!")


# Fungsi untuk menunjukkan menu management tugas Teacher
def show_assignment_manage_menu():
    os.system('cls')
    while True:
        assignments = assignment.get_all()
        if assignments['count'] != 0:
            print(f"Ada {assignments['count']} tugas:")

            assignment_table = PrettyTable(["ID", "JUDUL TUGAS", "BATAS WAKTU"])
            for index, item in enumerate(assignments["assignments"]):
                assignment_table.add_row(
                    [item['id'], item['title'], item['due_date'] if len(item['due_date']) != 0 else '-'])
            print(assignment_table)

            print()
            print("Petunjuk:")
            print("1. Masukkan id tugas untuk melihat rincian tugas")
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
                                while True:
                                    assignment_due_date_input = input("Batas waktu tugas (dd-mm-yyyy hh.mm): ")
                                    try:
                                        assignment_due_date = datetime.strptime(assignment_due_date_input,
                                                                                "%d-%m-%Y %H.%M")
                                        break
                                    except ValueError:
                                        print("Silakan masukkan batas waktu sesuai format")
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


# Fungsi untuk menunjukkan menu management Student data bagi Teacher
def show_student_detail(id):
    os.system('cls')
    while True:
        student_id = int(id)
        student_detail = student.get_detail(student_id)

        if student_detail is not None:

            print(student_detail["name"])
            print(student_detail["nim"])
            print()

            print("[1] Ubah nama mahasiswa")
            print("[2] Ubah NIM")
            print("[3] Hapus mahasiswa")
            print("[4] Kembali ke menu sebelumnya")

            selected_menu = input("Silakan pilih menu >> ").upper()
            match selected_menu:
                case "1":
                    os.system('cls')
                    _name = input("Masukkan nama baru (kosongkan jika ingin membatalkan) >> ")

                    nim = student_detail["nim"]

                    name = _name if len(_name) != 0 else student_detail["name"]

                    student_update = student.update(
                        student_id,
                        {"nim": nim, "name": name}
                    )

                    if student_update:
                        os.system('cls')
                        print("Nama berhasil diubah!")
                        print()
                    else:
                        os.system('cls')
                        print("Nama gagal diubah!")
                        print()

                    show_student_detail(student_id)

                case "2":
                    os.system('cls')
                    _nim = input("Masukkan NIM baru (kosongkan jika ingin membatalkan) >> ")

                    name = student_detail["name"]

                    nim = _nim if len(_nim) != 0 else student_detail["nim"]

                    student_update = student.update(
                        student_id,
                        {"nim": nim, "name": name}
                    )

                    if student_update:
                        os.system('cls')
                        print("NIM berhasil diubah!")
                        print()
                    else:
                        os.system('cls')
                        print("NIM gagal diubah!")
                        print()

                    show_student_detail(student_id)
                case "3":
                    delete_decision = input(
                        "Yakin ingin menghapus siswa ini? (y/n) >> ").upper()
                    match delete_decision:
                        case "Y":
                            student_delete = student.delete(student_id+1)
                            if student_delete:
                                os.system('cls')
                                print("Mahasiswa berhasil dihapus!")
                                print()
                            else:
                                os.system('cls')
                                print("Mahasiswa gagal dihapus!")
                                print()
                        case "N":
                            os.system('cls')
                            print("Operasi dibatalkan")
                    show_student_manage_menu()
                case "4":
                    show_student_manage_menu()
        else:
            print("Siswa tidak ditemukan!")


# Fungsi untuk menunjukkan menu show Student data bagi Teacher
def show_student_manage_menu():
    os.system('cls')
    while True:
        print("DAFTAR SISWA")
        student.show_students_as_table()

        print()
        print("Petunjuk:")
        print("1. Masukkan id siswa untuk melihat detail siswa")
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
                case "B":
                    show_main_menu()


# Fungsi untuk menunjukkan menu utama Teacher
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
