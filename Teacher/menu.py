import common_modules.global_menu as main_menu
from common_modules import csv, global_variable


def show_main_menu():
    while True:

        print("[1] Tampilkan daftar siswa")
        print("[2] Tampilkan daftar tugas")
        print("[3] Keluar dari akun")

        selected_menu = input("Silakan pilih menu >> ")
        match selected_menu:
            case "1":
                csv.show('database/students.csv')
                print()
            case "2":
                print()
            case "3":
                global_variable.session.clear()
                main_menu.show_roles_menu()
