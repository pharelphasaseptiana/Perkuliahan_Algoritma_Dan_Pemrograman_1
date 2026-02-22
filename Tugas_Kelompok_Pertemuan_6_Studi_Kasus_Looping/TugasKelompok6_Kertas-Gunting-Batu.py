import random

opsi = ["batu", "gunting", "kertas"]
skor_user = 0
skor_komputer = 0

print("=== Game Batu Gunting Kertas ===")

for ronde in range(1, 6):
    print(f"\nRonde {ronde}")
    pilihan = input("Pilih (batu/gunting/kertas): ").lower()
    komputer = random.choice(opsi)
    print("Komputer memilih:", komputer)

    if pilihan == komputer:
        print("Seri!")
    elif (pilihan == "batu" and komputer == "gunting") or \
         (pilihan == "gunting" and komputer == "kertas") or \
         (pilihan == "kertas" and komputer == "batu"):
        print("Kamu menang!")
        skor_user += 1
    else:
        print("Kamu kalah!")
        skor_komputer += 1

print("\n=== Hasil Akhir ===")
print("Skor Kamu:", skor_user)
print("Skor Komputer:", skor_komputer)

if skor_user > skor_komputer:
    print("🎉 Kamu MENANG total!")
elif skor_user < skor_komputer:
    print("😢 Kamu KALAH total!")
else:
    print("🤝 Seri total!")