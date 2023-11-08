import common_modules.global_menu as main_menu
from Teacher.assignment import show_all
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
                assignments = show_all()
                if assignments['count'] != 0:
                    print(f"Ada {assignments['count']} tugas")

                    for index, item in enumerate(assignments["assignments"]):
                        print(f"{index + 1}. {item['title']}")

                    print("Petunjuk:")
                    print("1. Masukkan nomor tugas untuk melihat rincian tugas")
                    print("2. + untuk menambahkan tugas")
                    print("3. B untuk kembali ke menu sebelumnya")
                    print('Asku telah disini')
                else:
                    print("Belum ada tugas yang dibuat")
                    print()
                    print("Petunjuk:")
                    print("1. + untuk menambahkan tugas")
                    print("2. B untuk kembali ke menu sebelumnya")
            case "3":
                global_variable.session.clear()
                main_menu.show_roles_menu()
