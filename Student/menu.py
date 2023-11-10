import os

from Student import assignment
from common_modules import global_variable, global_menu


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

    student_work = input(f"Silakan ketik SAYA SUDAH MENGERJAKAN TUGAS INI untuk menyelesaikan tugas\n>> ")

    match student_work:
        case "SAYA SUDAH MENGERJAKAN TUGAS INI":
            assignment.do(id, student_id)
        case _:
            print("TUGAS DITOLAK. Silakan kerjakan dengan cara yang sesuai.")

    show_main_menu()


def show_main_menu():
    os.system('cls')
    while True:

        assignments = assignment.get_individual_assignments(global_variable.session["nim"])
        print(assignments)
        print("Beranda Utama Siswa")
        print()
        print(global_variable.session["name"])
        print(global_variable.session["nim"])
        print()

        # print(status)
        # student_assignment_status = []
        # for index, item in enumerate(assignments):
        #     student_assignment_status.append(assignment.get_status(item["id"], global_variable.session["nim"]))
        #     print(f"{index} {item['title']}")
        #
        # for item in student_assignment_status:
        #     print(item[0]['status'])

        # status = assignment.get_status(assignments[])

        print()
        print("Petunjuk:")
        print("1. Masukkan nomor tugas untuk mengerjakan")
        print("2. U untuk keluar dari akun")

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
