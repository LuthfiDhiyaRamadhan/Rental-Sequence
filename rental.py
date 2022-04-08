##jam_masuk=int(input     ("Jam Masuk     :"))
##menit_masuk=int(input  ("Menit Masuk     :"))
##jam_keluar=int(input     ("Jam Keluar  :"))
##menit_keluar=int(input  ("Menit Keluar  :"))
import math

print("Selamat Datang Di Rental Python")
print("=========================================================")
print("Biaya Rental = 5000/Jam")
print("=========================================================")
jam_masuk,menit_masuk=input("Waktu Masuk (hh:mm) :"). split(":")
jam_keluar,menit_keluar=input("Waktu Keluar (hh:mm) :"). split(":")
jam_masuk = int(jam_masuk)
menit_masuk = int(menit_masuk)
jam_keluar = int(jam_keluar)
menit_keluar = int(menit_keluar)

masuk= jam_masuk * 60
menitmasuk = masuk + menit_masuk

keluar= jam_keluar * 60
menitkeluar = keluar + menit_keluar

menit= menitkeluar-menitmasuk
jam= menit // 60
menitjam= menit % 60
biaya_rental = 5000* menit / 60
print(f"Lama Rental          : {menit} Menit ({jam} Jam {menitjam} Menit )")
print(f"Biaya Rental Asli    : Rp. {biaya_rental :2.0f}")
biaya_rental = round(biaya_rental, -3)
print(f"Biaya Rental Biasa   : Rp. {biaya_rental}") ##pembulatan biasa
biaya_rental=math.ceil(biaya_rental/1000)*1000
print(f"Biaya Rental A       : Rp. {biaya_rental}") ##pembulatan keatas
biaya_rental=math.floor(biaya_rental/100)*100
print(f"Biaya Rental B       : Rp. {biaya_rental}") ##pembulatan kebawah

