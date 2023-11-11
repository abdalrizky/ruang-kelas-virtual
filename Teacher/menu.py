import os
from datetime import datetime

from prettytable import PrettyTable

import common_modules.global_menu as main_menu
from Teacher import assignment, student
from common_modules import global_variable


# Fungsi untuk menampilkan rincian tugas berdasarkan id
def show_assignment_detail(id):
    os.system('cls')

    assignment_id = int(id)

    # Ambil rincian tugas berdasarkan id
    assignment_detail = assignment.get_detail(assignment_id)

    # Jika tugas yang dimaksud ada
    if assignment_detail is not None:

        # Ambil status pengerjaan tugas berdasarkan id tugas
        assignment_status = assignment.get_status(assignment_id)

        print(assignment_detail['title'])
        print()
        print("Deskripsi:")
        print(assignment_detail['description'])
        print()
        print(
            f"Batas waktu: {(assignment_detail['due_date'] if len(assignment_detail['due_date']) != 0 else 'Tidak ada')} ")

        print()

        # Tampilkan daftar siswa yang mengerjakan tugas, jika tidak ada tampilkan '-'
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

                # Variabel sementara untuk menampung nilai input title
                _title = input("Masukkan judul tugas baru (kosongkan apabila ingin membatalkan) >> ")

                # Karena field selain title tidak diubah, ambil due_date dan description berdasarkan data awal
                due_date = assignment_detail["due_date"]
                description = assignment_detail["description"]

                # Jika _title berisi karakter, tetapkan menjadi nilai title, apabila tidak, ambil berdasarkan data awal
                title = _title if len(_title) != 0 else assignment_detail["title"]

                # Proses update assignment
                assignment_update = assignment.update(
                    assignment_id,
                    {"title": title, "description": description, "due_date": due_date}
                )

                # Jika update assignment berhasil, print pesan berhasil
                if assignment_update:
                    os.system('cls')
                    print("Judul berhasil diubah!")

            case "2":
                os.system('cls')

                # Variabel sementara untuk menampung nilai input description
                _description = input("Masukkan deskripsi tugas baru (kosongkan apabila ingin membatalkan) >> ")

                # Karena field selain decription tidak diubah, ambil due_date dan title berdasarkan data awal
                due_date = assignment_detail["due_date"]
                title = assignment_detail["title"]

                # Jika _description berisi karakter, tetapkan menjadi nilai description, apabila tidak, ambil berdasarkan data awal
                description = _description if len(_description) != 0 else assignment_detail["description"]

                # Proses update assignment
                assignment_update = assignment.update(
                    assignment_id,
                    {"title": title, "description": description, "due_date": due_date}
                )

                # Jika update assignment berhasil, print pesan berhasil
                if assignment_update:
                    os.system('cls')
                    print("Deskripsi tugas berhasil diubah!")

            case "3":
                os.system('cls')
                while True:
                    # Variabel sementara untuk menampung nilai input _due_date
                    _due_date = input("Masukkan batas waktu baru dd-mm-yyyy hh.mm (kosongkan apabila ingin "
                                      "membatalkan) >> ")

                    try:
                        # Jika _due_date berisi karakter, konversikan menjadi objek datetime
                        if len(_due_date) != 0:
                            _due_date = datetime.strptime(_due_date, "%d-%m-%Y %H.%M")
                        break

                    # Jika proses konversi ke objek datetime gagal, minta guru untuk memasukkan format yang benar
                    except ValueError:
                        print("Silakan masukkan batas waktu sesuai format")

                # Karena field selain due_date tidak diubah, ambil title dan description berdasarkan data awal
                title = assignment_detail["title"]
                description = assignment_detail["description"]

                # Jika _due_date berisi karakter, tetapkan menjadi nilai due_date, apabila tidak, ambil berdasarkan data awal
                due_date = _due_date if len(str(_due_date)) != 0 else assignment_detail["due_date"]

                # Proses update assignment
                assignment_update = assignment.update(
                    assignment_id,
                    {"title": title, "description": description, "due_date": due_date}
                )

                # Jika update assignment berhasil, print pesan berhasil
                if assignment_update:
                    os.system('cls')
                    print("Batas waktu tugas berhasil diubah!")

            case "4":
                delete_decision = input("Yakin ingin menghapus tugas ini? (y/n) >> ").upper()
                match delete_decision:
                    case "Y":
                        # Proses hapus tugas
                        assignment_delete = assignment.delete(assignment_id)

                        # Jika hapus tugas berhasil, tampilkan pesan berhasil
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
        # Proses mengambil tugas dari database
        assignments = assignment.get_all()

        # Jika tugas ada, tampilkan tabel tugas
        if assignments['count'] != 0:
            print(f"Ada {assignments['count']} tugas:")

            # Deklarasi PrettyTable
            assignment_table = PrettyTable(["ID", "JUDUL TUGAS", "BATAS WAKTU"])

            for index, item in enumerate(assignments["assignments"]):
                # Tambahkan baris pada tabel
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

        # Periksa apakah inputan adalah angka
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
                                    # Coba konversikan input ke objek datetime, apabila gagal, minta user untuk input
                                    # batas waktu kembali
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

                    # Proses membuat tugas
                    create_assignment = assignment.create(
                        assignment_title,
                        assignment_description,
                        assignment_due_date
                    )

                    # Jika tugas berhasil dibuat, tampilkan pesan berhasil
                    if create_assignment:
                        os.system('cls')
                        print("Tugas berhasil ditambahkan!")

                case "B":
                    show_main_menu()


# Fungsi untuk menunjukkan menu management Student data bagi Teacher
def show_student_detail(id):
    os.system('cls')
    while True:
        student_id = int(id)

        # Proses mengambil detail siswa berdasarkan id siswa
        student_detail = student.get_detail(student_id)

        # Jika siswa ditemukan di database, tampilkan detail
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

                    # Variabel sementara untuk menampung input nama
                    _name = input("Masukkan nama baru (kosongkan jika ingin membatalkan) >> ")

                    # Karena NIM tidak diubah, maka ambil NIM berdasarkan data awal
                    nim = student_detail["nim"]

                    # Tetapkan _name sebagai nilai dari name jika _name berisi karakter, jika tidak, ambil berdasarkan
                    # data awal
                    name = _name if len(_name) != 0 else student_detail["name"]

                    # Proses ubah data siswa
                    student_update = student.update(
                        student_id,
                        {"nim": nim, "name": name}
                    )

                    # Jika update data siswa berhasil, tampilkan pesan berhasil
                    if student_update:
                        os.system('cls')
                        print("Nama berhasil diubah!")
                        print()

                    # Kembali ke detail siswa tersebut
                    show_student_detail(student_id)

                case "2":
                    os.system('cls')

                    # Variabel sementara untuk menampung input nim
                    _nim = input("Masukkan NIM baru (kosongkan jika ingin membatalkan) >> ")

                    # Karena name tidak diubah, maka ambil name berdasarkan data awal
                    name = student_detail["name"]

                    # Tetapkan _nim sebagai nilai dari name jika _nim berisi karakter, jika tidak, ambil berdasarkan
                    # data awal
                    nim = _nim if len(_nim) != 0 else student_detail["nim"]

                    student_update = student.update(
                        student_id,
                        {"nim": nim, "name": name}
                    )

                    # Jika update data siswa berhasil, tampilkan pesan berhasil
                    if student_update:
                        os.system('cls')
                        print("NIM berhasil diubah!")
                        print()

                    show_student_detail(student_id)
                case "3":
                    delete_decision = input(
                        "Yakin ingin menghapus siswa ini? (y/n) >> ").upper()
                    match delete_decision:
                        case "Y":
                            # Proses hapus siswa
                            student_delete = student.delete(student_id)
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
        print("DAFTAR MAHASISWA")

        # Tampilkan semua siswa dalam bentuk tabel
        student.show_as_table()

        print()
        print("Petunjuk:")
        print("1. Masukkan id siswa untuk melihat detail siswa")
        print("2. + untuk menambahkan siswa")
        print("3. B untuk kembali ke menu sebelumnya")

        selected_menu = input("Silakan pilih menu >> ").upper()
        # Apabila input berupa angka
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
                    while True:
                        student_id = input("NIM: ")
                        # Coba konversi nim ke integer, apabila gagal, minta pengguna memasukkan kembali
                        try:
                            int(student_id)
                            break
                        except ValueError:
                            print("NIM harus angka!")

                    # Proses menambah siswa
                    add_student = student.add(
                        student_name,
                        student_id
                    )

                    # Jika proses tambah siswa berhasil, tampilkan pesan berhasil
                    if add_student:
                        os.system('cls')
                        print("Siswa berhasil ditambahkan!")

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
                # Menghapus sesi yang tersimpan
                global_variable.session.clear()

                os.system('cls')
                main_menu.show_roles_menu()
