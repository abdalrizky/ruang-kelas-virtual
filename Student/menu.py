import os

from prettytable import PrettyTable

from Student import assignment
from common_modules import global_variable, global_menu


# Fungsi untuk mengerjakan penugasan
def do_assignment(id, student_id):
    os.system('cls')
    assignment_detail = assignment.get_detail(id)

    print(assignment_detail["title"])
    print()
    print("Deskripsi:")
    print(assignment_detail["description"])
    print()
    print(
        f"Kamu bisa mengerjakan tugas ini sampai dengan {assignment_detail['due_date'] if len(assignment_detail['due_date']) != 0 else '-'}")

    student_work = input(
        f"Silakan ketik SAYA SUDAH MENGERJAKAN TUGAS INI untuk menyelesaikan tugas (kosongkan untuk membatalkan)\n>> ")

    match student_work:
        case "SAYA SUDAH MENGERJAKAN TUGAS INI":
            assignment.do(id, student_id)
            os.system('cls')
            print("Tugas telah diselesaikan!")
            print()
        case _:
            os.system('cls')
            print("TUGAS DITOLAK. Silakan kerjakan dengan cara yang sesuai.")
            print()

    show_main_menu()


# Fungsi untuk menunjukkan menu Student
def show_main_menu():
    os.system('cls')
    while True:

        print("Beranda Utama Siswa")
        print()
        print(global_variable.session["name"])
        print(global_variable.session["nim"])
        print()

        assignments = assignment.get_assignments(global_variable.session["nim"])
        if len(assignments) != 0:
            table = PrettyTable(["ID", "NAMA TUGAS", "BATAS WAKTU", "STATUS"])
            for index, item in enumerate(assignments):
                table.add_row([index, item['title'], item['due_date'] if len(item['due_date']) != 0 else '-',
                               'SUDAH DIKERJAKAN' if item['status'] == 'finish' else 'BELUM DIKERJAKAN'])
            print(table)

            print()
            print("Petunjuk:")
            print("1. Masukkan nomor tugas untuk mengerjakan")
            print("2. U untuk keluar dari akun")
        else:
            print("Belum ada tugas")
            print()
            print("Petunjuk:")
            print("1. U untuk keluar dari akun")

        selected_menu = input("Silakan pilih menu >> ").upper()
        if selected_menu.lstrip("-").isdigit():
            if int(selected_menu) >= 0:
                do_assignment(selected_menu, global_variable.session["nim"])
            else:
                print("Silakan masukkan angka yang valid")
        else:
            match selected_menu:
                case "U":
                    global_variable.session.clear()
                    os.system('cls')
                    global_menu.show_roles_menu()
