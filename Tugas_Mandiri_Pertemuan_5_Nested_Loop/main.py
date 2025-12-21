# 1. Pola angka menurun
print("1. Pola angka menurun:")
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # pindah baris

# 2. Pola segitiga kiri
print("\n2. Pola segitiga kiri:")
for i in range(1, 6):
    print("*" * i)

# 3. Pola persegi
print("\n3. Pola persegi:")
for i in range(5):
    print("*" * 5)