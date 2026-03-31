#nomor 1
def input_dan_tampilkan():
    teks = input("Masukkan sesuatu: ")
    print("Kamu memasukkan:", teks)
input_dan_tampilkan()

#nomor 2
def tampilkan_input(pesan):
    data = input(pesan)
    print("Hasil input:", data)
tampilkan_input("Masukkan nama: ")
tampilkan_input("Masukkan umur: ")

#nomor 3
def ambil_input():
    data = input("Masukkan sesuatu: ")
    return data

hasil = ambil_input()
print("Isi variabel hasil:", hasil)
print("Tipe data:", type(hasil))

#nomor 4
def input_float(pesan):
    nilai = float(input(pesan))
    return nilai

angka = input_float("Masukkan angka desimal: ")
print("Nilai yang dimasukkan:", angka)
print("Tipe data:", type(angka))

#nomor 5
import math
def hitung_sisi_miring():
    a = float(input("Masukkan panjang sisi alas (a): "))
    b = float(input("Masukkan panjang sisi tinggi (b): "))
    hypo = math.sqrt(a**2 + b**2)
    print("Sisi miring (hypo) =", hypo)

hitung_sisi_miring()

#nomor 6

import math
def hitung_sisi_miring():
    a = float(input("Masukkan sisi alas: "))
    b = float(input("Masukkan sisi tinggi: "))
    print("Sisi miring =", math.sqrt(a**2 + b**2))

hitung_sisi_miring()

#nomor 7
nama_depan = "Budi"
nama_belakang = "Santoso"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

#nomor 8
teks = "Halo "
print(teks * 3)

#nomor 9
angka = 10
teks = str(angka)
print(teks)
print(type(teks))

#nomor 10
angka = 10
teks = str(angka)
print(teks)
print(type(teks))

#nomor 11
# Input dari user
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
# Operasi matematika
print("Hasil penjumlahan:", a + b)
print("Hasil pengurangan:", a - b)
print("Hasil pembagian:", a / b)
print("Hasil perkalian:", a * b)
# Kalimat penutup
print("Selamat kamu sudah pintar matematika")

#nomor 12
x = float(input("Masukkan nilai x: "))
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print("Nilai y =", y)

#nomor 13
jam = int(input("Waktu mulai (jam): "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))
total_menit = jam * 60 + menit + durasi
jam_selesai = (total_menit // 60) % 24
menit_selesai = total_menit % 60
print("Acara berakhir pukul {:02d}:{:02d}".format(jam_selesai,
menit_selesai))
