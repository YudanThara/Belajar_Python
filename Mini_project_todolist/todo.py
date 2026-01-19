import os

daftar = []
riwayat = []

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

console_clear()

def kembali_ke_menu():
    print("\n")
    input(">> Tekan [Enter] untuk kembali ke menu...")
    console_clear()

def mengulangi_input():
    print("\n")
    input(">> Tekan [Enter] untuk mengulangi...")
    console_clear()

def menu():
    print(f"""{'='*25}
Menu Pilihan:
[1] Lihat Tugas
[2] Tambah Tugas
[3] Ubah Status
[4] Hapus Tugas
[5] Reset Tugas
[6] Riwayat Tugas
[7] Keluar
{'='*25}
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
        while True:
            print(f"{'='*5} Menambahkan tugas baru {'='*5}\n")
            print(">> Ketik [0] Nol untuk kembali ke menu utama\n") 
            input_kegiatan = input("> Masukkan nama tugas: ").strip()
            if input_kegiatan == "0":
                return
            if not input_kegiatan:
                print("\n>> [!] Error: Nama tugas tidak boleh kosong!")
                mengulangi_input()
            else:
                break

        status_final = ""
        while True:
            console_clear()
            print(f"{'='*5} Menambahkan tugas baru {'='*5}\n")
            print(">> Ketik [0] Nol untuk kembali ke menu utama\n") 
            print(f"Kegiatan: {input_kegiatan}")
            print("""\nStatus Tugas:
[1] Selesai
[2] Sedang dikerjakan
[3] Belum selesai (default)
""")
            input_status = input("> Pilih status tugas (Enter untuk default): ").strip()
            if input_status == "1": 
                status_final = "Selesai"
                break
            elif input_status == "2": 
                status_final = "Sedang dikerjakan"
                break
            elif input_status == "3" or input_status == "":
                status_final = "Belum selesai"
                break
            elif input_status == "0":
                return
            else: 
                print("\n>> [!] Pilihan tidak valid! Masukkan angka 1-3 atau 0 untuk kembali")
                mengulangi_input()

        prioritas_final = ""
        while True:
            console_clear()
            print(f"{'='*5} Menambahkan tugas baru {'='*5}\n")
            print(">> Ketik [0] Nol untuk kembali ke menu utama\n") 
            print(f"Kegiatan: {input_kegiatan}")
            print(f"Status: {status_final}")
            print("""\nPrioritas Tugas:
[1] Tinggi
[2] Sedang (default)
[3] Rendah
""")
            input_prioritas = input("> Pilih prioritas tugas: ").strip()
            if input_prioritas == "1":
                prioritas_final = "Tinggi"
                break
            elif input_prioritas == "2" or input_prioritas == "":
                prioritas_final = "Sedang"
                break
            elif input_prioritas == "3":
                prioritas_final = "Rendah"
                break
            elif input_prioritas == "0":
                return
            else:
                print("\n>> [!] Pilihan tidak valid! Masukkan angka 1-3 atau 0 untuk kembali")
                mengulangi_input()

        tugas_baru = {
        'Kegiatan': input_kegiatan,
        'Status': status_final,
        'Prioritas': prioritas_final
        }

        daftar.append(tugas_baru)
        print(f"\n>> [Berhasil] {input_kegiatan} | {status_final} | Prioritas: {prioritas_final}")
        break

def Ubah_Status():
    if len(daftar) == 0:
        print("\nDaftar tidak tersedia")
        return
    while True:
        print(f"{'='*5} Mengubah status tugas {'='*5}\n")
        print(">> Ketik [0] Nol untuk kembali ke menu utama\n")
        try:
            Lihat_Tugas()
            input_ubah = int(input("\n> Pilih nomor status yang akan diubah menjadi selesai: "))
            if input_ubah == 0:
                return
            indeks = input_ubah - 1
            if 0 <= indeks < len(daftar):
                daftar[indeks]['Status'] = "Selesai"
                nama_kegiatan = daftar[indeks]['Kegiatan']
                print(f"\n>> [v] Status kegiatan {nama_kegiatan} berhasil diubah\n")
                break
            else:
                print("\n>> [!] Pilihan tidak valid! Masukkan angka yang ada dalam daftar\n")
                mengulangi_input()
        except ValueError:
            print("\n>> [!] Pilihan tidak valid! Input harus berupa angka")
            mengulangi_input()

def Hapus_Tugas():
    if len(daftar) == 0:
        print("\nDaftar tidak tersedia")
        return
    while True:
        print(f"{'='*5} Menghapus tugas {'='*5}\n")
        print(">> Ketik [0] Nol untuk kembali ke menu utama\n")
        try:
            Lihat_Tugas()
            hapus = int(input("\n> Pilih nomor tugas yang akan dihapus: "))
            if hapus == 0:
                return
            indeks = hapus -1
            if 0 <= indeks < len(daftar):
                item_yang_dihapus = daftar.pop(indeks)
                riwayat.append(item_yang_dihapus)
                nama_kegiatan = item_yang_dihapus['Kegiatan']
                print(f"\n>> [v] Kegiatan {nama_kegiatan} berhasil dihapus\n")
                break
            else:
                print("\n>> [!] Pilihan tidak valid! Masukkan angka yang ada dalam daftar\n")
                mengulangi_input()
        except ValueError:
            print("\n>> [!] Pilihan tidak valid! Input harus berupa angka")
            mengulangi_input()

def Reset_Tugas():
    if len(daftar) == 0:
        print("Daftar tidak tersedia")
        return
    while True:
        print(f"{'='*5} Mereset semua tugas {'='*5}\n")
        input_reset = input("> [PERINGATAN] Apakah anda yakin? (y/n): ")
        if input_reset.lower() == "y":
            riwayat.extend(daftar)
            daftar.clear()
            print("\nDaftar berhasil di reset")
            break
        elif input_reset.lower() == "n":
            print("\nBatal")
            break
        else:
            print("\n>> [!] Pilihan tidak tersedia! harap ketik 'y' atau 'n'")
            mengulangi_input()

def Riwayat_Tugas():
    print(f"{'='*5} Melihat riwayat tugas yang sudah dihapus {'='*5}\n")
    print("Daftar tugas:")
    if len(riwayat) == 0:
        print("Daftar tidak tersedia")
        return
    else:
        for position, i in enumerate(riwayat, start = 1):
            print(f"{position}. {i['Kegiatan']} | {i['Status']} | {i['Prioritas']}")

while True:
    try:
        menu()
        pilihan = int(input("\n> Masukkan pilihan anda: "))
        if pilihan == 1:
            console_clear()
            print(f"{'='*5} Melihat daftar tugas {'='*5}\n")
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
            console_clear()
            Riwayat_Tugas()
            kembali_ke_menu()
        elif pilihan == 7:
            print("\n>> Terima kasih telah menggunakan aplikasi ini!")
            exit()
        else: 
            print("\n>> [!] Pilihan tidak valid! Masukkan angka yang ada dalam menu")
            kembali_ke_menu()
    except ValueError:
            print("\n>> [!] Pilihan tidak valid! Input harus berupa angka")
            kembali_ke_menu()