# Meminta input bilangan bulat dari pengguna
bilangan = int(input("Masukkan bilangan bulat: "))

# Mengecek kondisi bilangan
if bilangan > 0:
    print("Bilangan positif")
elif bilangan < 0:
    print("Bilangan negatif")
else:
    print("Bilangan nol")

# Meminta input nilai angka dari pengguna
nilai = int(input("Masukkan nilai angka (0-100): "))

# Mengecek rentang nilai dan menentukan nilai huruf
if 85 <= nilai <= 100:
    print("Nilai huruf: A")
elif 70 <= nilai <= 84:
    print("Nilai huruf: B")
elif 55 <= nilai <= 69:
    print("Nilai huruf: C")
elif 40 <= nilai <= 54:
    print("Nilai huruf: D")
elif 0 <= nilai < 40:
    print("Nilai huruf: E")
else:
    print("Nilai tidak valid")

# Meminta input total belanja
total_belanja = float(input("Masukkan total belanja: Rp "))

# Menentukan diskon berdasarkan total belanja
if total_belanja >= 500000:
    diskon = 0.2 * total_belanja
elif total_belanja >= 250000:
    diskon = 0.1 * total_belanja
else:
    diskon = 0

# Menghitung total bayar
total_bayar = total_belanja - diskon

# Menampilkan hasil
print("\n=== Rincian Pembayaran ===")
print(f"Total Belanja : Rp {total_belanja:,.0f}")
print(f"Diskon        : Rp {diskon:,.0f}")
print(f"Total Bayar   : Rp {total_bayar:,.0f}")