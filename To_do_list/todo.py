import os

daftar = []

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

console_clear()

def kembali_ke_menu():
    print("\n")
    input("Tekan [Enter] untuk kembali ke menu...")
    console_clear()

def mengulangi_input():
    print("\n")
    input("Tekan [Enter] untuk mengulangi...")
    console_clear()

def menu():
    print(f"""{"="*20}
Menu Pilihan:
1. Lihat Tugas
2. Tambah Tugas
3. Hapus Tugas
4. Reset Tugas
5. Keluar
{"="*20}
    """)

def Lihat_Tugas():
    print("Daftar tugas:\n")
    if len(daftar) == 0:
        print("Daftar tidak tersedia")
        return
    else:
        for position, i in enumerate(daftar, start = 1):
            print(position, i)

def Tambah_Tugas():
    while True:
        print("Menambahkan tugas baru\n")
        tugas_baru = input("Mau tugas apa?: ").strip()
        if not tugas_baru:
            print("\nTugas tidak boleh kosong")
            mengulangi_input()
        else:
            daftar.append(tugas_baru)
            print(f"\n{tugas_baru} berhasil ditambahkan\n")
            break

def Hapus_Tugas():
    if len(daftar) == 0:
        print("\nDaftar tidak tersedia")
        return
    while True:
        try:
            print("Menghapus tugas\n")
            Lihat_Tugas()
            hapus = int(input("\nPilih satu tugas yang ingin dihapus: "))
            indeks = hapus -1
            if 0 <= indeks < len(daftar):
                daftar.pop(indeks)
                print("\nTugas berhasil dihapus\n")
                break
            else:
                print("\nTugas tidak ada dalam daftar\n")
                mengulangi_input()
        except ValueError:
            print("\nPilihan tidak tersedia")
            mengulangi_input()

def Reset_Tugas():
    if len(daftar) == 0:
        print("Daftar tidak tersedia")
        return
    while True:
        print("Mereset semua tugas\n")
        input_reset = input("Apakah anda yakin? (y/n)")
        if input_reset.lower() == "y":
            daftar.clear()
            print("\nDaftar berhasil di reset")
            break
        elif input_reset.lower() == "n":
            print("\nBatal")
            break
        else:
            print("\nPilihan tidak tersedia, harap ketik 'y' atau 'n'")
            mengulangi_input()

while True:
    try:
        menu()
        pilihan = int(input("\nMasukkan pilihan anda: "))
        if pilihan == 1:
            console_clear()
            Lihat_Tugas()
            kembali_ke_menu()
        elif pilihan == 2:
            console_clear()
            Tambah_Tugas()
            kembali_ke_menu()
        elif pilihan == 3:
            console_clear()
            Hapus_Tugas()
            kembali_ke_menu()
        elif pilihan == 4:
            console_clear()
            Reset_Tugas()
            kembali_ke_menu()
        elif pilihan == 5:
            print("\nTerima kasih telah menggunakan aplikasi ini")
            exit()
        else: 
            print("\nPilihan tidak tersedia")
            kembali_ke_menu()
    except ValueError:
            print("\nInput harus berupa angka")
            kembali_ke_menu()