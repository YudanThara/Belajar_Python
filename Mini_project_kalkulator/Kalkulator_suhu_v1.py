# Kalkulator Suhu v1

# Konversi suhu dari celcius hingga kelvin
# Dengan memilih pilihan a, b, c, d, e

# Menampilkan judul
print("==================")
print("Kalkulator Suhu v1")
print("==================\n")

o = "Pilih suhu yang akan diubah"
# Menampilkan daftar pilihan
a = "a. Celcius"
b = "b. Reamur"
c = "c. Fahrenheit"
d = "d. Kelvin"
e = "e. Keluar"

# Celcius
celcius1 = "1. Celcius ke Reamur"
celcius2 = "2. Celcius ke Fahrenheit"
celcius3 = "3. Celcius ke Kelvin"
celcius4 = "4. Kembali ke pilihan lain"

# Reamur
reamur1 = "1. Reamur ke Celcius"
reamur2 = "2. Reamur ke Fahrenheit"
reamur3 = "3. Reamur ke Kelvin"
reamur4 = "4. Kembali ke pilihan lain"

# Fahrenheit
fahrenheit1 = "1. Fahrenheit ke Celcius"
fahrenheit2 = "2. Fahrenheit ke Reamur"
fahrenheit3 = "3. Fahrenheit ke Kelvin"
fahrenheit4 = "4. Kembali ke pilihan lain"

# Kelvin
kelvin1 = "1. Kelvin ke Celcius"
kelvin2 = "2. Kelvin ke Reamur"
kelvin3 = "3. Kelvin ke Fahrenheit"
kelvin4 = "4. Kembali ke pilihan lain"

# Menampilkan daftar pilihan
print(f"{o}\n{a}\n{b}\n{c}\n{d}\n{e}")
# Input untuk memilih pilihan
data = str(input("Masukkan pilihan anda: ").lower())

# Program
while True:
    # Pilihan celcius
    if data == "a":
        print(f"\n{celcius1}\n{celcius2}\n{celcius3}\n{celcius4}")
        data_celcius = int(input("Masukkan pilihan anda: "))
        if data_celcius == 1:
            print("\nCelcius ke Reamur")
            celcius = float(input("Masukkan angka: "))
            reamur = (4 / 5) * celcius
            print(f"{celcius} Celcius = {reamur} Reamur")
        elif data_celcius == 2:
            print("\nCelcius ke Fahrenheit")
            celcius = float(input("Masukkan angka: "))
            fahrenheit = (9 / 5) * celcius + 32
            print(f"{celcius} Celcius = {fahrenheit} Fahrenheit")
        elif data_celcius == 3:
            print("\nCelcius ke Kelvin")
            celcius = float(input("Masukkan angka: "))
            kelvin = celcius + 273.15
            print(f"{celcius} Celcius = {kelvin} Kelvin")
        elif data_celcius == 4:
            print(f"\n{o}\n{a}\n{b}\n{c}\n{d}\n{e}")
            data = str(input("Masukkan pilihan anda: ").lower())
        else:
            print("\nPilihan tidak tersedia")
    # Pilihan reamur
    elif data == "b":
        print(f"\n{reamur1}\n{reamur2}\n{reamur3}\n{reamur4}")
        data_reamur = int(input("Masukkan pilihan anda: "))
        if data_reamur == 1:
            print("\nReamur ke Celcius")
            reamur = float(input("Masukkan angka: "))
            celcius = (5 / 4) * reamur
            print(f"{reamur} Reamur = {celcius} Celcius")
        elif data_reamur == 2:
            print("\nReamur ke Fahrenheit")
            reamur = float(input("Masukkan angka: "))
            fahrenheit = (9 / 4) * reamur + 32
            print(f"{reamur} Reamur = {fahrenheit} Fahrenheit")
        elif data_reamur == 3:
            print("\nReamur ke Kelvin")
            reamur = float(input("Masukkan angka: "))
            kelvin = (5 / 4) * reamur + 273.15
            print(f"{reamur} Reamur = {kelvin} Kelvin")
        elif data_reamur == 4:
            print(f"\n{o}\n{a}\n{b}\n{c}\n{d}\n{e}")
            data = str(input("Masukkan pilihan anda: ").lower())
        else:
            print("\nPilihan tidak tersedia")
    # Pilihan fahrenheit
    elif data == "c":
        print(f"\n{fahrenheit1}\n{fahrenheit2}\n{fahrenheit3}\n{fahrenheit4}")
        data_fahrenheit = int(input("Masukkan pilihan anda: "))
        if data_fahrenheit == 1:
            print("\nFahrenheit ke Celcius")
            fahrenheit = float(input("Masukkan angka: "))
            celcius = (5 / 9) * (fahrenheit - 32)
            print(f"{fahrenheit} Fahrenheit = {celcius} Celcius")
        elif data_fahrenheit == 2:
            print("\nFahrenheit ke Reamur")
            fahrenheit = float(input("Masukkan angka: "))
            reamur = (4 / 9) * (fahrenheit - 32)
            print(f"{fahrenheit} Fahrenheit = {reamur} Reamur")
        elif data_fahrenheit == 3:
            print("\nFahrenheit ke Kelvin")
            fahrenheit = float(input("Masukkan angka: "))
            kelvin = (5 / 9) * (fahrenheit - 32) + 273.15
            print(f"{fahrenheit} Fahrenheit = {kelvin} Kelvin")
        elif data_fahrenheit == 4:
            print(f"\n{o}\n{a}\n{b}\n{c}\n{d}\n{e}")
            data = str(input("Masukkan pilihan anda: ").lower())
        else:
            print("\nPilihan tidak tersedia")
    # Pilihan kelvin
    elif data == "d":
        print(f"\n{kelvin1}\n{kelvin2}\n{kelvin3}\n{kelvin4}")
        data_kelvin = int(input("Masukkan pilihan anda: "))
        if data_kelvin == 1:
            print("\nKelvin ke Celcius")
            kelvin = float(input("Masukkan angka: "))
            celcius = kelvin - 273.15
            print(f"{kelvin} Kelvin = {celcius} Celcius")
        elif data_kelvin == 2:
            print("\nKelvin ke Reamur")
            kelvin = float(input("Masukkan angka: "))
            reamur = (4 / 5) * (kelvin - 273.15)
            print(f"{kelvin} Kelvin = {reamur} Reamur")
        elif data_kelvin == 3:
            print("\nKelvin ke Fahrenheit")
            kelvin = float(input("Masukkan angka: "))
            fahrenheit = (9 / 5) * (kelvin - 273.15) + 32
            print(f"{kelvin} Kelvin = {fahrenheit} Fahrenheit")
        elif data_kelvin == 4:
            print(f"\n{o}\n{a}\n{b}\n{c}\n{d}\n{e}")
            data = str(input("Masukkan pilihan anda: ").lower())
        else:
            print("\nPilihan tidak tersedia")
    # Pilihan keluar
    elif data == "e":
        print("\nKeluar")
        break
    # Pilihan tidak tersedia
    else:
        print("\nPilihan tidak tersedia")
        print(f"\n{o}\n{a}\n{b}\n{c}\n{d}\n{e}")
        data = str(input("Masukkan pilihan anda: ").lower())
# Program selesai
print("\nTerima kasih~")