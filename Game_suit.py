import random

def main():
    pilihan = ["batu", "gunting", "kertas"]
    skor_pemain = 0
    skor_komputer = 0

    print("=== Game Suit - Batu Gunting Kertas ===")
    print("Ketik 'exit' untuk keluar.\n")

    while True:
        pemain = input("Pilih (batu/gunting/kertas): ").lower()

        if pemain == "exit":
            print("Game selesai. Sampai jumpa!")
            break

        if pemain not in pilihan:
            print("Pilihan tidak valid, coba lagi ya 😅")
            continue

        komputer = random.choice(pilihan)
        print(f"Komputer memilih: {komputer}")

        if pemain == komputer:
            print("Seri! 😐")
        elif (
            (pemain == "batu" and komputer == "gunting") or
            (pemain == "gunting" and komputer == "kertas") or
            (pemain == "kertas" and komputer == "batu")
        ):
            print("Kamu menang! 😎")
            skor_pemain += 1
        else:
            print("Kamu kalah! 😭")
            skor_komputer += 1

        print(f"Skor: Kamu {skor_pemain} - Komputer {skor_komputer}\n")

main()