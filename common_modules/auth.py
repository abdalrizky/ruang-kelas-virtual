from common_modules import global_variable, query


# Fungsi untuk memproses login guru
def login_as_teacher(username, password):
    teacher_credential = global_variable.login_teacher[0]
    if username == teacher_credential["username"] and password == teacher_credential["password"]:
        global_variable.session = {
            "role": "teacher",
            "name": teacher_credential["username"].capitalize(),
            "username": username,
        }
        return True


# Fungsi untuk memproses login siswa
def login_as_student(nim, password):
    result = query.search_nim(nim)
    if result is not None:
        if nim == result["nim"] and password == "mhs":
            global_variable.session = {
                "role": "student",
                "name": result["name"],
                "nim": result["nim"],
            }
            return True
    else:
        return False
