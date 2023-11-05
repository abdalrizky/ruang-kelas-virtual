from Student.assignment import get_assignments
from common_modules import global_variable, global_menu


def show_main_menu():
    while True:

        assignments = get_assignments()

        print("Beranda Utama Siswa")
        print()
        print(global_variable.session["name"])
        print(global_variable.session["nim"])
        print()

        # Tampilkan tugas
        if assignments["count"] != 0:
            print("Daftar Tugas")
            for index, item in enumerate(assignments["assignments"]):
                print(
                    f"{index + 1}. {assignments['assignments'][index]['name']} {assignments['assignments'][index]['status']} {assignments['assignments'][index]['grade']}")
        else:
            print("Belum ada tugas")

        print()
        print("Petunjuk:")
        print("1. Masukkan nomor tugas untuk mengerjakan")
        print("2. U untuk keluar dari akun")

        selected_menu = input("Silakan pilih menu >> ").upper()
        match selected_menu:
            case "U":
                global_variable.session.clear()
                global_menu.show_roles_menu()
