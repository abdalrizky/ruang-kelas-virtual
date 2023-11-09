import common_modules.global_menu as main_menu
from Teacher import assignment
from common_modules import csv, global_variable


def show_assignment_detail(selected_menu):

    assignment_id = int(selected_menu)-1
    assignment_detail = assignment.get_detail(assignment_id)[0]

    if assignment_detail is not None:

        assignment_status = assignment.get_status(assignment_id)

        print(f"{assignment_detail['title']}")
        print(f"Batas waktu: {(assignment_detail['due_date'] if len(assignment_detail['due_date']) != 0 else 'Tidak ada')} ")

        print("Siswa yang sudah mengerjakan tugas ini:")
        # finished = [student for student in assignment_status if assignment_status["assignment_id"] == str(assignment_id)]
        # print(finished)
        # for index, item in enumerate(assignment_status):
        #     print(f"{index+1}. {item}")

        print("Petunjuk:")
        print("1. E untuk mengubah nama tugas")
        print("2. ED untuk mengubah batas waktu")
        print("3. - untuk menghapus tugas")
        print("4. B untuk kembali ke menu sebelumnya")
        selected_menu = input("Silakan pilih menu >> ").upper()
        match selected_menu:
            case "E":
                print()
            case "ED":
                print()
            case "-":
                print()
            case "B":
                show_assignment_manage_menu()
    else:
        print("Tugas tidak ditemukan!")


def show_assignment_manage_menu():
    while True:
        assignments = assignment.get_all()
        if assignments['count'] != 0:
            print(f"Ada {assignments['count']} tugas:")

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

        selected_menu = input("Silakan pilih menu >> ").upper()
        if selected_menu.lstrip("-").isdigit():
            if int(selected_menu) >= 1:
                show_assignment_detail(selected_menu)
            else:
                print("Silakan masukkan angka yang valid")
        else:
            match selected_menu:
                case "+":
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
                                break
                            case _:
                                print("Pilihan tidak ada")

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
