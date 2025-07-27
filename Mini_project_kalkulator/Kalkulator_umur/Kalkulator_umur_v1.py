# date and tine

import datetime as dt

print("Kalkulator Umur Sederhana\n")

tanggal = int(input("Masukkan tangal lahir anda: \t"))
bulan = int(input("Masukkan bulan lahir anda: \t"))
tahun = int(input("Masukkan tahun lahir anda: \t"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"\nTanggal lahir anda adalah: {tanggal_lahir}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_bulan = umur_hari.days // 30
umur_tahun = umur_hari.days // 365

umur_bulan_sisa = (umur_hari.days % 365) // 30
umur_hari_sisa = (umur_hari.days % 365) & 30

print(f"Umur anda adalah: {umur_hari.days} hari")
print(f"Umur anda adalah: {umur_bulan} bulan")
print(f"Umur anda adalah: {umur_tahun} tahun")

print(f"\nTotal umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan, {umur_hari_sisa} hari")
