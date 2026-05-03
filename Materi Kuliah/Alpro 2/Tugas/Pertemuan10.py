# NO1
# pangkat = [x ** 2 for x in range(10)]
# print(pangkat)
# dua_pangkat = [2 ** i for i in range(8)]
# print(dua_pangkat)
# ganjil = [x for x in pangkat if x % 2 != 0]
# print(ganjil)
# genap = [x for x in pangkat if x % 2 == 0]
# print(genap)

#NO 2
# papan_catur = []
# KOSONG = "."
# for i in range(8):
#     baris = [KOSONG for i in range(8)]
#     papan_catur.append(baris)
# print(papan_catur)

# # contoh 2:
# papan_catur = [["KOSONG" for i in range(8)] for j in range(8)]

# papan_catur[0][0] = "Benteng"
# papan_catur[0][7] = "Benteng"
# papan_catur[7][0] = "Benteng"
# papan_catur[7][7] = "Benteng"

# papan_catur[4][2] = "Kuda"
# print("\noutput no 2: ")
# print("-------------------------")
# print("Isi kotak [4][2]:", papan_catur[4][2])
# print("Isi kotak [0][0]:", papan_catur[0][0])
# print("Isi kotak [0][7]:", papan_catur[0][7])
# print("Isi kotak [7][0]:", papan_catur[7][0])
# print("Isi kotak [7][7]:", papan_catur[7][7])

#nomor 3
# print("--output list multidimensi--")

# hotel = [[[False for kamar in range(20)] 
#           for lantai in range(15)] 
#           for gedung in range(3)]

# # contoh isi kamar (gedung 2, lantai 10, kamar 14)
# hotel[1][9][13] = True

# # contoh kamar kosong (gedung 1, lantai 5, kamar 2)
# hotel[0][4][1] = False

# print(hotel[1][9][13])

# #nomor 4
# # fungsi berparamenter
# def pesan(angka):
#     print("Masukan sebuah angka: ", angka)
# pesan(3)

# #fungsi berparamenter
# def pesan(angka):
#     print("Masukan sebuah angka teman: ", angka)
# angka = 12222222
# pesan(5)
# print(angka)

# # positional argumen passing
# def perkenalan(nama_depan, nama_belakang):
#     print("Halo perkenenalkan nama saya: ", nama_depan, nama_belakang)

# perkenalan("SO", "JUNGHWAN")
# perkenalan("KIM", "EUNHA")

# #keyword argumen passing
# def perkenalan(nama_depan, nama_belakang):
#     print("Halo perkenenalkan nama saya: ", nama_depan, nama_belakang)
    
# perkenalan(nama_depan="PARK", nama_belakang="JEONGWOO")
# perkenalan(nama_depan="KIM", nama_belakang="JUNKYU")

# # mixing passing
# def penjumlahan(a,b,c):
#     print(a, "+", b, "+", c, "=", a+b+c)

# penjumlahan(1,2,3)
# penjumlahan(c=1, a=2, b=3)
# penjumlahan(a=3, c=1, b=2)
# penjumlahan(c=3, a=1, b=2)

# # Fungsi 3 parameter
# def alamat(jalan, kota, kodepos):
#     print("Alamat anda di ", "Jl. ", jalan, "Kota/Kab.", kota, "Kodepos: ", kodepos)
# jln = input("Masukan nama jalan: ")
# kt = input("Masukan nama Kab/Kota: ")
# kp = input("Masukan nama Kodepos: ")
# alamat(jln, kt, kp)

# # pre define
# def nama(nama_depan, nama_belakang="HONG"):
#     print(nama_depan, nama_belakang)

# nama("Hein")
# print("SOOBIN", "BAEK")

# #nomor 5
# hasil = [x * 3 for x in range(1,11) if x % 2 == 0]
    
# print(hasil)

# #nomor 6
# array = [[i*3+j+1 for j in range(3)] for i in range(3)]

# for barisan in array:
#     print(barisan)

# #nomor 7
# data = [[2,4], [6,8], [10,12]]

# flat = [elemen for baris in data for elemen in baris]

# print(flat)

#nomor 8
print("\noutput soal no 8: ")
print("menghitung luas persegi panjang")
# p dan l di sini adalah PARAMETER
def cetak_luas(p, l):
    print(f"Luas dengan panjang {p} dan lebar {l} adalah: {p * l}")

cetak_luas(3, 5)
cetak_luas(10, 8)
