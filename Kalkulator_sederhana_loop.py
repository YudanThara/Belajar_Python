# Kalkulator sederhana 2 angka v2
# dengan penambahan looping

# Penjumlahan, pengurangan, perkalian, pembagian
# Dengan pilihan a, b, c, d

# Menampilkab judul
print("====================")
print("Kalkulator sederhana")
print("====================")
print("Menggunakan pilihan a, b, c, d, e\n")

# Daftar pilihan menu
a = "a. Penjumlahan (+)"
b = "b. Pengurangan (-)"
c = "c. Perkalian   (*)"
d = "d. Pembagian   (/)"
e = "e. Keluar      (X)"

# Menampilkan daftar pilihan
print(f"{a}\n{b}\n{c}\n{d}\n{e}")

# Program kalkulator
while True: # jika True maka perulangan akan terus berjalan
    # Input pilihan dari pengguna
    data = str(input("Masukkan pilihan anda: ").lower())
    if data == "a":
        print("\nPenjumlahan")
        # Input 2 angka dari pengguna
        jumlah1 = float(input("Masukkan angka pertama: "))
        jumlah2 = float(input("Masukkan angka kedua: "))
        # Menampilkan hasil penjumlahan
        print(f"{jumlah1} + {jumlah2} = {jumlah1 + jumlah2}\n")
    elif data == "b":
        print("\nPengurangan")
        kurang1 = float(input("Masukkan angka pertama: "))
        kurang2 = float(input("Masukkan angka kedua: "))
        # Menampilkan hasil pengurangan
        print(f"{kurang1} - {kurang2} = {kurang1 - kurang2}\n")
    elif data == "c":
        print("\nPerkalian")
        kali1 = float(input("Masukkan angka pertama: "))
        kali2 = float(input("Masukkan angka kedua: "))
        # Menampilkan hasil perkalian
        print(f"{kali1} x {kali2} = {kali1 * kali2}\n")
    elif data == "d":
        print("\nPembagian")
        bagi1 = float(input("Masukkan angka pertama: "))
        bagi2 = float(input("Masukkan angka kedua: "))
        # Jika pembagian dengan angka 0, tampilkan pesan error
        if bagi2 == 0:
            print("Pembagian dengan angka 0 tidak dapat dilakukan\n")
        else:
            # Jika pembagian bukan dengan angka 0, lakukan pembagian
            # Menampilkan hasil pembagian
            print(f"{bagi1} / {bagi2} = {bagi1 / bagi2}\n")
    elif data == "e":
        print("\nKeluar")
        break # menghentikan perulangan jika data = "e"
    else:
        # Jika pilihan tidak tersedia, tampilkan pesan error
        print("Pilihan tidak tersedia\n")
# Program selesai
print("\nTerima kasih")