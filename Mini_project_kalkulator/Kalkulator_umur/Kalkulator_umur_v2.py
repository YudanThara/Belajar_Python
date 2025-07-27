# date and tine

# Kalkulator Umur v2
# dengan penambahan pilihan dan perulangan
# kalkulator ini belum mencapai keakurtan 100%

# Import modul datetime untuk menghitung umur
import datetime as dt

# Menampilkan judul
print("Kalkulator Umur Sederhana\n")

# Input tanggal lahir
print("Masukkan tanggal, bulan, tahun lahir anda")
tanggal = int(input("Masukkan tangal lahir anda: \t"))
bulan = int(input("Masukkan bulan lahir anda: \t"))
tahun = int(input("Masukkan tahun lahir anda: \t"))

# Membuat tanggal lahir
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"\nTanggal lahir anda adalah: {tanggal_lahir}")

# Menampilkan menu pilihan
print('''
1. Umur dalam hari
2. Umur dalam bulan
3. Umur dalam tahun
4. Total umur
5. Keseluruhan umur dan total
6. Memasukkan tanggal lahir baru
7. Keluar
      ''')

# Perulangan program
while True:
    # Input pilihan
    data = str(input("Masukkan pilihan anda: "))

    # Tanggal hari ini
    hari_ini = dt.date.today()

    # Menghitung umur
    umur_hari = hari_ini - tanggal_lahir
    umur_bulan = umur_hari.days // 30
    umur_tahun = umur_hari.days // 365

    # Informasi tanggal lahir
    hari_lahir = tanggal_lahir.strftime("%A")
    bulan_lahir = tanggal_lahir.strftime("%B")
    tahun_lahir = tanggal_lahir.strftime("%Y")

    # Menghitung sisa bulan dan hari
    umur_bulan_sisa = (umur_hari.days % 365) // 30
    umur_hari_sisa = (umur_hari.days % 365) % 30

    # Pilihan menu
    if data == "1":
        print("\nHitung umur dalam hari")
        print(f"Umur anda adalah: {umur_hari.days} hari")
        print(f"Lahir pada hari: {hari_lahir}\n")
    elif data == "2":
        print("\nHitung umur dalam bulan")
        print(f"Umur anda adalah: {umur_bulan} bulan")
        print(f"Lahir pada bulan: {bulan_lahir}\n")
    elif data == "3":
        print("\nHitung umur dalam tahun")
        print(f"Umur anda adalah: {umur_tahun} tahun\n")
        print(f"Lahir pada tahun: {tahun_lahir}\n")
    elif data == "4":
        print(f"\nTotal umur anda adalah: \n{umur_tahun} tahun \n{umur_bulan_sisa} bulan \n{umur_hari_sisa} hari\n")
    elif data == "5":
        print("\nMenghitung keseluruhan umur dan total")
        print(f"Umur anda adalah: {umur_hari.days} hari")
        print(f"Umur anda adalah: {umur_bulan} bulan")
        print(f"Umur anda adalah: {umur_tahun} tahun")
        print(f"Total umur anda adalah: \n{umur_tahun} tahun \n{umur_bulan_sisa} bulan \n{umur_hari_sisa} hari\n")
    elif data == "6":
        # Input ulang tanggal lahir
        print("\nMemasukkan tanggal lahir baru")
        tanggal = int(input("Masukkan tangal lahir anda: \t"))
        bulan = int(input("Masukkan bulan lahir anda: \t"))
        tahun = int(input("Masukkan tahun lahir anda: \t"))
        tanggal_lahir = dt.date(tahun,bulan,tanggal)
        print(f"\nTanggal lahir anda adalah: {tanggal_lahir}\n")
    elif data == "7":
        # Keluar dari program
        print("\nKeluar")
        break
    else:
        print("\nPilihan tidak tersedia")

# Program selesai
print("\nTerima kasih~")