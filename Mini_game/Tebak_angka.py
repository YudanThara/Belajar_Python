import random
import os

main_lagi = "y"

while main_lagi == "y":
    angka_rahasia = random.randint(1, 50)
    percobaan = 0

    os.system("cls" if os.name == "nt" else "clear")
    
    print("""
===== Selamat datang di permainan tebak angka! =====

Tebak angka antara 1 sampai 50
Dengan 10 kali percobaan!
""")

    while percobaan < 10:
        try:
            angka_tebakan = int(input("\nTebak angka: "))
        except ValueError:
            print("Masukkan angka yang valid ya!")
            continue

        percobaan += 1

        if angka_tebakan < angka_rahasia:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Salah, angka {angka_tebakan} terlalu kecil")
            print(f"Sisa percobaan: {10 - percobaan}")
        elif angka_tebakan > angka_rahasia:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Salah, angka {angka_tebakan} terlalu besar")
            print(f"Sisa percobaan: {10 - percobaan}")
        else:
            print("\n🎉 Selamat, tebakan kamu BENAR! 🎉")
            break
    else:
        print(f"\n💀 Percobaan habis! Angka rahasianya adalah {angka_rahasia} 💀")

    while True:
        main_lagi = input("\nMau main lagi? (y/n): ").strip().lower()
        if main_lagi == "y" or main_lagi == "n":
            break
        else:
            print("Masukkan pilihan yang benar ya!")

print("\nTerima kasih sudah bermain!❤️")