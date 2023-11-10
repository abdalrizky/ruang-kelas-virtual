import os

from Student.menu import show_main_menu as show_student_menu
from Teacher.menu import show_main_menu as show_teacher_menu
from common_modules import auth


def show_welcome_message():
    os.system('cls')
    print("""
   _____      _                       _         _       _                    _ 
  / ____|    | |                     | |       | |     | |                  | |
 | (___   ___| | __ _ _ __ ___   __ _| |_    __| | __ _| |_ __ _ _ __   __ _| |
  \___ \ / _ \ |/ _` | '_ ` _ \ / _` | __|  / _` |/ _` | __/ _` | '_ \ / _` | |
  ____) |  __/ | (_| | | | | | | (_| | |_  | (_| | (_| | || (_| | | | | (_| |_|
 |_____/ \___|_|\__,_|_| |_| |_|\__,_|\__|  \__,_|\__,_|\__\__,_|_| |_|\__, (_)
                                                                        __/ |  
                                                                       |___/   
""")
    show_roles_menu()


def show_roles_menu():

    while True:

        print("Login sebagai?")
        print("[1] Guru")
        print("[2] Siswa")
        print("[3] Keluar dari program")

        selected_menu = input("Silakan pilih menu >> ")
        match selected_menu:
            case "1":

                show_login_form("teacher")
            case "2":

                show_login_form("student")
            case "3":
                exit()


def show_login_form(role):
    os.system('cls')
    match role:
        case "teacher":
            while True:

                print("Untuk masuk ke dasbor, kamu perlu login terlebih dahulu.")
                print()
                print("Petunjuk:")
                print("Username dan password gunakan \"admin\"")
                print()

                username = input("Username >> ")
                password = input("Kata sandi >> ")

                login_result = auth.login_as_teacher(username, password)
                if login_result:
                    show_teacher_menu()
                else:
                    print("Username atau password salah.")

        case "student":
            while True:

                print("Untuk masuk ke dasbor, kamu perlu login terlebih dahulu.")
                print("Petunjuk:")
                print("1. Login menggunakan NIM")
                print("2. Password \"mhs\"")

                nim = input("NIM >> ")
                password = input("Kata sandi >> ")
                login_result = auth.login_as_student(nim, password)
                if login_result:
                    show_student_menu()
                else:
                    print("Username atau password salah.")
