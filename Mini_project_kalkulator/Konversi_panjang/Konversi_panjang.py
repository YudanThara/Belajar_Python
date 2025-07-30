# Kalkulator Konversi Panjang Sederhana

# Menampilkan judul
print("===========================")
print("Kalkulator Konversi Panjang")
print("===========================\n")

# Dictionary konversi ke meter
konversi_panjang = {
    "km" : 1000,
    "hm" : 100,
    "dam" : 10,
    "m" : 1,
    "dm" : 0.1,
    "cm" : 0.01,
    "mm" : 0.001,
    "inch" : 0.0254,
    "feet" : 0.3048,
    "yard" : 0.9144,
    "mile" : 1609.34
}

# Menampilkan daftar satuan yang tersedia
print("Satuan yang tersedia: ")
for satuan in konversi_panjang:
    print(f"- {satuan}")

# Loop utama program
while True:
    print("\nKetik 'exit' untuk keluar")
    
    # Input satuan asal
    dari = input("Dari satuan: \t").lower()
    if dari == "exit":
        print("\nSelamat tinggal~")
        break
    
    # Input satuan tujuan
    ke = input("Ke satuan: \t").lower()
    if ke == "exit":
        print("\nSelamat tinggal~")
        break

    # Proses konversi jika satuan valid
    if dari in konversi_panjang and ke in konversi_panjang:
        nilai = float(input("Masukkan nilai: "))
        
        # Konversi nilai ke meter
        meter = nilai * konversi_panjang[dari]
        
        # Konversi meter ke satuan tujuan
        hasil = meter / konversi_panjang[ke]
        
        # Tampilkan hasil konversi
        print(f"{nilai} {dari} = {hasil:.4f} {ke}")
    
    else:
        # Pesan jika satuan tidak dikenal
        print("Satuan tidak dikenal, silakan coba lagi ya~")
