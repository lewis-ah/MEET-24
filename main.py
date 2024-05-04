import fisika
import time

import fisika.JualBeli

def batas():
    print("-"*15)
    
waktu_awal = time.time()
print(f"Massa Jenis = {fisika.MassaJenis.MassaJenis(10,2)}")
print(f"Massa = {fisika.MassaJenis.Massa(10,2)}")
print(f"Volume = {fisika.MassaJenis.Volume(10,2)}")

waktu_akhir = time.time()
print(f"waktu yang dibutuhkan : {waktu_akhir - waktu_awal}")

batas()
print(f"Usaha = {fisika.U(12,3)}")
print(f"Usaha = {fisika.G(6,2)}")
print(f"Usaha = {fisika.J(10,2)}")

batas()

print(f" Hasil Energi Potensial : {fisika.Ep(4,7,4)}")
print(f"Hasil Energi Kinetik : {fisika.Ek(4, 7)}")
batas()

diskon10 = fisika.jl(10)
result = diskon10(10000)
print(f"Diskon 10% = {result}")