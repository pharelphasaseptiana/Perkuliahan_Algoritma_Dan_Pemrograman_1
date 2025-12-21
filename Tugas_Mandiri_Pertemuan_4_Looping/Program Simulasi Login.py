# Kredensial benar
USERNAME_BENAR = "admin"
PASSWORD_BENAR = "python"

maks_percobaan = 3
percobaan = 0

while percobaan < maks_percobaan:
    print(f"Percobaan ke-{percobaan + 1} dari {maks_percobaan}")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username == USERNAME_BENAR and password == PASSWORD_BENAR:
        print("Login berhasil! Selamat datang.")
        break
    else:
        percobaan += 1
        sisa = maks_percobaan - percobaan
        if sisa > 0:
            print(f"Login gagal")