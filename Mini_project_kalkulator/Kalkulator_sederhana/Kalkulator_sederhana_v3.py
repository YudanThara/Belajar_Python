# Kalkulator sederhana 2 angka v3
# dengan penambahan def, try except

# Penjumlahan, pengurangan, perkalian, pembagian
# Dengan pilihan a, b, c, d

import os

# Menampilkab judul
def header():
    '''fungsi untuk menampilkan header'''
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'Kalkulator sederhana':^40}")
    print(f"{'Menggunakan pilihan a, b, c, d':^40}\n")

    # Daftar pilihan menu
    print("Pilih menu:")
    print(f"{'a. Penjumlahan (+)':<30}")
    print(f"{'b. Pengurangan (-)':<30}")
    print(f"{'c. Perkalian   (*)':<30}")
    print(f"{'d. Pembagian   (/)':<30}")

def penjumlahan(angka1, angka2):
    '''fungsi penjumlahan'''
    print(f"{angka1} + {angka2} = {angka1 + angka2}")
    return angka1 + angka2

def pengurangan(angka1, angka2):
    '''fungsi pengurangan'''
    print(f"{angka1} - {angka2} = {angka1 - angka2}")
    return angka1 - angka2

def perkalian(angka1, angka2):
    '''fungsi perkalian'''
    print(f"{angka1} * {angka2} = {angka1 * angka2}")
    return angka1 * angka2

def pembagian(angka1, angka2):
    '''fungsi pembagian'''
    if angka2 == 0:
        return "Pembagian dengan angka 0 tidak dapat dilakukan"
    else:
        print(f"{angka1} / {angka2} = {angka1 / angka2}")
        return angka1 / angka2

def try_except(error):
    '''fungsi untuk menangani error'''
    while True:
        try:
            return error()
        except ValueError:
            print("Input tidak valid")

def input_user():
    '''fungsi untuk input angka dari pengguna'''
    angka1 = try_except(lambda: float(input("Masukkan angka pertama: ")))
    angka2 = try_except(lambda: float(input("Masukkan angka kedua: ")))
    return angka1, angka2

# Menampilkan daftar pilihan

# Program kalkulator
while True: # jika True maka perulangan akan terus berjalan
    header()
    data = input("Pilih menu (a/b/c/d): ").lower().strip()  # Mengambil input dari pengguna dan mengubahnya menjadi huruf kecil

    # Input pilihan dari pengguna
    if data == "a":
        print("\nPenjumlahan")
        # Input 2 angka dari pengguna
        angka1, angka2 = input_user()
        # Menampilkan hasil penjumlahan
        penjumlahan(angka1, angka2)
    elif data == "b":
        print("\nPengurangan")
        angka1, angka2 = input_user()
        pengurangan(angka1, angka2)
    elif data == "c":
        print("\nPerkalian")
        angka1, angka2 = input_user()
        perkalian(angka1, angka2)
    elif data == "d":
        print("\nPembagian")
        angka1, angka2 = input_user()
        # Jika pembagian dengan angka 0, tampilkan pesan error
        if angka2 == 0:
            print("Pembagian dengan angka 0 tidak dapat dilakukan\n")
        else:
            # Jika pembagian bukan dengan angka 0, lakukan pembagian
            pembagian(angka1, angka2)
    else:
        # Jika pilihan tidak tersedia, tampilkan pesan error
        print("Pilihan tidak tersedia\n")
    
    # Menanyakan kepada pengguna apakah ingin melanjutkan
    while True:
        ulang = input("\nApakah Anda ingin melanjutkan? (y/n): ").lower().strip()
        if ulang == "y":
            break
        elif ulang == "n":
            # Program selesai
            print("\nTerima kasih")
            exit()
        else:
            print("Input tidak valid")
            continue
