#Nomor 1
x=0
y=1
z=0
print(x==y)
print(x==z)
print(x!=y)
print(x!=z)
print(x<y)
print(y<z)
print(x>y)
print(y>z)
print(x<=y)
print(x<=z)
print(y<=z)
print(x>=y)
print(x>=z)
print(y>=z)

#nomor 2
n = int(input("Masukkan nilai n: "))
if n < 100:
    print(False)
elif n > 100:
    print(True)

#nomor 3
n = int(input("Masukkan nilai n: "))
if n < 100:
    print(False)
elif n > 100:
    print(True)

#nomor 4
x = 10
if x > 5: #kondisi 1
    print("x lebih besar dari 5") # dieksekusi jika kondisi 1 bernilai true
if x < 10: #kondisi 2
    print("x lebih kecil dari 10") # dieksekusi jika kondisi 2 bernilai true
if x == 10: #kondisi 3
    print("x sama dengan 10") # dieksekusi jika kondisi 3 bernilai true

#nomor 5
x = 10
if x > 5: #kondisi 1
    print("x lebih besar dari 10") # dieksekusi jika kondisi 1 bernilai true
else:
    print("x lebih besar atau sama dengan 10") # dieksekusi jika kondisi bernilai false

#nomor 6
x = 10
if x == 10:
    print("x == 10")
elif x > 15:
    print("x > 15")
elif x > 10 :
    print("x > 10")
elif x > 5:
    print("x > 5")
else:
    print("x lebih kecil dari 5")

#nomor 7

#membaca 2 angka
angka1 = int (input("Masukkan angka pertama: "))
angka2 = int (input("Masukkan angka kedua: "))

#memilih angka yang besar
if angka1 > angka2:
    angka_besar = angka1
else:
    angka_besar = angka2
#print hasil
print("angka paling besar adalah", angka_besar)

#soal 8
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))
terbesar = a
if b > terbesar:
    terbesar = b

if c > terbesar:
    terbesar = c
print("Angka terbesar adalah:", terbesar)

#soal 9

#membaca 3 angka
angka1 = int (input("Masukkan angka pertama: "))
angka2 = int (input("Masukkan angka kedua: "))
angka3 = int (input("Masukkan angka ketiga: "))
#cek angka paling besar
angka_besar = max(angka1,angka2,angka3)
#print hasil
print("angka paling besar adalah", angka_besar)

#soal 10
pendapatan = int(input("Masukkan pendapatan per tahun (Rupiah): "))

if pendapatan <= 60000000:
    pajak = pendapatan * 0.05
elif pendapatan <= 250000000:
    pajak = pendapatan * 0.15
elif pendapatan <= 500000000:
    pajak = pendapatan * 0.25
else:
    pajak = pendapatan * 0.30

print("Pendapatan:", pendapatan)
print("Pajak yang harus dibayar:", pajak)
