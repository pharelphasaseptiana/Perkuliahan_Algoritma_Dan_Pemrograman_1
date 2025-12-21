# =========================
# SOAL 1 — Menyimpan dan Membaca Biodata
# =========================

# input biodata
nama = input("Nama : ")
nim = input("NIM  : ")
prodi = input("Prodi: ")

# simpan ke file
with open("biodata.txt", "w") as f:
    f.write(nama + "," + nim + "," + prodi)

# baca kembali file
with open("biodata.txt", "r") as f:
    data = f.read()

# pecah data berdasarkan koma
nama, nim, prodi = data.split(",")

# tampilkan hasil
print("\n=== HASIL BIODATA ===")
print("Nama :", nama)
print("NIM  :", nim)
print("Prodi:", prodi)


# =========================
#  2 — Log Aktivitas Sederhana (Append Mode)
# =========================

from datetime import datetime

# ambil waktu saat ini
waktu = datetime.now().strftime("%H:%M")

# tulis log aktivitas (append)
with open("log.txt", "a") as f:
    f.write("[" + waktu + "] Program dijalankan\n")

print("\nLog aktivitas telah ditambahkan.")


# =========================
# SOAL 3 — Rekap Nilai Mahasiswa (Format CSV Sederhana)
# =========================

# input jumlah data mahasiswa
jumlah = int(input("\nJumlah mahasiswa: "))

# simpan data ke file
with open("nilai_mahasiswa.txt", "w") as f:
    for i in range(jumlah):
        print("\nData mahasiswa ke-" + str(i+1))
        nama = input("Nama        : ")
        tugas = input("Nilai Tugas : ")
        uts = input("Nilai UTS   : ")
        uas = input("Nilai UAS   : ")

        # format CSV sederhana
        f.write(nama + "," + tugas + "," + uts + "," + uas + "\n")

# baca file dan tampilkan rekap
print("\n=== REKAP NILAI MAHASISWA ===")
print("Nama   Tugas   UTS   UAS   Rata2")

with open("nilai_mahasiswa.txt", "r") as f:
    for line in f:
        line = line.strip()
        nama, tugas, uts, uas = line.split(",")

        # hitung rata-rata
        rata = (float(tugas) + float(uts) + float(uas)) / 3

        print(nama, " ", tugas, "    ", uts, "   ", uas, "   ", round(rata, 2))
