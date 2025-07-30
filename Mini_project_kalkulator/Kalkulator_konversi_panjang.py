# Konversi panjang

print("===========================")
print("Kalkulator Konversi Panjang")
print("===========================\n")

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

print("Satuan yang tersedia: ")
for satuan in konversi_panjang:
    print(f"- {satuan}")

while True:
    print("\nKetik 'exit' untuk keluar")
    dari = input("Dari satuan: \t").lower()
    if dari.lower() == "exit":
        print("\nSelamat tinggal~")
        break
    ke = input("Ke satuan: \t").lower()
    if ke.lower() == "exit":
        print("\nSelamat tinggal~")
        break

    if dari in konversi_panjang and ke in konversi_panjang:
        nilai = float(input("Masukkan nilai: "))
        meter = nilai * konversi_panjang[dari]
        hasil = meter / konversi_panjang[ke]
        print(f"{nilai} {dari} = {hasil:.4f} {ke}")
    else:
        print("Satuan tidak dikenal, silakan coba lagi ya~")