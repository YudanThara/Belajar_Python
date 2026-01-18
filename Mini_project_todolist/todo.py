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
[1] Lihat Tugas
[2] Tambah Tugas
[3] Ubah Status
[4] Hapus Tugas
[5] Reset Tugas
[6] Keluar
{"="*20}
    """)

def Lihat_Tugas():
    print("Daftar tugas:")
    if len(daftar) == 0:
        print("Daftar tidak tersedia")
        return
    else:
        for position, i in enumerate(daftar, start = 1):
            print(f"{position}. {i['Kegiatan']} | {i['Status']} | {i['Prioritas']}")

def Tambah_Tugas():
    while True:
        print(f"{"="*5} Menambahkan tugas baru {"="*5}\n")
        while True:
            input_kegiatan = input("Mau tugas apa?: ").strip()
            if not input_kegiatan:
                print(">> Error: Nama tugas tidak boleh kosong!")
                mengulangi_input()
            else:
                break

        status_final = ""
        while True:
            print("""\nStatus Tugas:
[1] Selesai
[2] Sedang dikerjakan
[3] Belum selesai (default)
Masukkan status tugas: 
""")
            input_status = input("Pilih status tugas (Enter untuk default): ").strip()
            if input_status == "1": 
                status_final = "Selesai"
                break
            elif input_status == "2": 
                status_final = "Sedang dikerjakan"
                break
            elif input_status == "3" or input_status == "":
                status_final = "Belum selesai"
                break
            else: 
                print("\n>> Pilihan tidak valid! Masukkan angka 1, 2, atau 3")
                mengulangi_input()

        prioritas_final = ""
        while True:
            print("""\nPrioritas Tugas:
[1] Tinggi
[2] Sedang (default)
[3] Rendah
""")
            input_prioritas = input("Pilih prioritas tugas: ").strip()
            if input_prioritas == "1":
                prioritas_final = "Tinggi"
                break
            elif input_prioritas == "2" or input_prioritas == "":
                prioritas_final = "Sedang"
                break
            elif input_prioritas == "3":
                prioritas_final = "Rendah"
                break
            else:
                print("\n>> Pilihan tidak valid! Masukkan angka 1, 2, atau 3")
                mengulangi_input()

        tugas_baru = {
        'Kegiatan': input_kegiatan,
        'Status': status_final,
        'Prioritas': prioritas_final
        }

        daftar.append(tugas_baru)
        print(f"\n[Berhasil] {input_kegiatan} | {status_final} | Prioritas: {prioritas_final}")
        break

def Ubah_Status():
    if len(daftar) == 0:
        print("\nDaftar tidak tersedia")
        return
    while True:
        try:
            print(f"{"="*5} Mengubah status tugas {"="*5}\n")
            Lihat_Tugas()
            input_ubah = int(input("\nPilih nomor status yang akan diubah menjadi selesai: "))
            indeks = input_ubah - 1
            if 0 <= indeks < len(daftar):
                daftar[indeks]['Status'] = "Selesai"
                nama_kegiatan = daftar[indeks]['Kegiatan']
                print(f"Status kegiatan {nama_kegiatan} berhasil diubah\n")
                break
            else:
                print("\n>> Pilihan tidak valid! Masukkan angka yang ada dalam daftar\n")
                mengulangi_input()
        except ValueError:
            print("\n>> Pilihan tidak valid! Input harus berupa angka")
            mengulangi_input()

def Hapus_Tugas():
    if len(daftar) == 0:
        print("\nDaftar tidak tersedia")
        return
    while True:
        try:
            print(f"{"="*5} Menghapus tugas {"="*5}\n")
            Lihat_Tugas()
            hapus = int(input("\nPilih nomor tugas yang akan dihapus: "))
            indeks = hapus -1
            if 0 <= indeks < len(daftar):
                item_yang_dihapus = daftar.pop(indeks)
                nama_kegiatan = item_yang_dihapus['Kegiatan']
                print(f"\nKegiatan {nama_kegiatan} berhasil dihapus\n")
                break
            else:
                print("\n>> Pilihan tidak valid! Masukkan angka yang ada dalam daftar\n")
                mengulangi_input()
        except ValueError:
            print("\n>> Pilihan tidak valid! Input harus berupa angka")
            mengulangi_input()

def Reset_Tugas():
    if len(daftar) == 0:
        print("Daftar tidak tersedia")
        return
    while True:
        print(f"{"="*5} Mereset semua tugas {"="*5}\n")
        input_reset = input("Apakah anda yakin? (y/n)")
        if input_reset.lower() == "y":
            daftar.clear()
            print("\nDaftar berhasil di reset")
            break
        elif input_reset.lower() == "n":
            print("\nBatal")
            break
        else:
            print("\n>> Pilihan tidak tersedia! harap ketik 'y' atau 'n'")
            mengulangi_input()

while True:
    try:
        menu()
        pilihan = int(input("\nMasukkan pilihan anda: "))
        if pilihan == 1:
            console_clear()
            print(f"{"="*5} Melihat daftar tugas {"="*5}\n")
            Lihat_Tugas()
            kembali_ke_menu()
        elif pilihan == 2:
            console_clear()
            Tambah_Tugas()
            kembali_ke_menu()
        elif pilihan == 3:
            console_clear()
            Ubah_Status()
            kembali_ke_menu()
        elif pilihan == 4:
            console_clear()
            Hapus_Tugas()
            kembali_ke_menu()
        elif pilihan == 5:
            console_clear()
            Reset_Tugas()
            kembali_ke_menu()
        elif pilihan == 6:
            print("\nTerima kasih telah menggunakan aplikasi ini!")
            exit()
        else: 
            print("\n>> Pilihan tidak valid! Masukkan angka yang ada dalam menu")
            kembali_ke_menu()
    except ValueError:
            print("\n>> Pilihan tidak valid! Input harus berupa angka")
            kembali_ke_menu()