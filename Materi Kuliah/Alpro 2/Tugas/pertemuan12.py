# #soal 1
# print("--soal 1--")
# def penjumlahan(x):
#     bilangan = 7
#     return x + 7

# print(penjumlahan(4))
# print(bilangan)

#soal 2
print("--soal 2--")
# Contoh 1
bilangan = 2
def perkalian_bilangan(x):
    return x * bilangan
 
print(perkalian_bilangan(7))

#soal 3
print("--soal 3--")
# Contoh 2
def perkalian_bilangan2(x):
    bilangan = 5          # variabel lokal, menutupi yang global
    return x * bilangan
 
print(perkalian_bilangan2(7))

#soal 4
print("--soal 4--")
bilangan = 2 
print(bilangan)

def return_bilangan():
    global bilangan
    bilangan = 5
    return bilangan

print(return_bilangan())
print(bilangan)

#soal 5
print("--soal 5--")
def hitung_imt(berat, tinggi):
    imt = berat / (tinggi ** 2)
    return imt

def kategori_imt(imt):
    if imt < 18.5:
        return "Berat badan kurang"
    elif imt >= 18.5 and imt < 25:
        return "Berat badan normal"
    elif imt >= 25 and imt < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"

# input dari user
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter): "))

# proses
imt = hitung_imt(berat, tinggi)
kategori = kategori_imt(imt)

# output
print("Nilai IMT kamu:", round(imt, 2))
print("Kategori:", kategori)

#soal 6
print("--soal 6--")
def cek_segitiga(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(cek_segitiga(1,1,1))
print(cek_segitiga(1,1,3))

#soal 7
print("--soal 7--")
def cek_segitiga(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(cek_segitiga(1,1,1))
print(cek_segitiga(1,1,3))

#soal 8
print("--soal 8--")
def cek_segitiga(a, b, c):
    return a + b > c and b + c > a and c + a > b
       
print(cek_segitiga(1,1,1))
print(cek_segitiga(1,1,3))

#soal 9
print("--soal 9--")
def faktorial(n):
    # Bilangan yang akan difaktorial harus lebih besar dari 0
    if n < 0:
        return None
    # 0! dan 1! nilainya sama (1)
    if n < 2:
        return 1
 
    hasil = 1
    for i in range(2, n + 1):   # dari 2 sampai n (inklusif)
        hasil = hasil * i        # kalikan hasil dengan i
    return hasil
 
n = int(input("Masukkan nilai yang ingin di faktorial: "))
print(n, "! =", faktorial(n))

#soal 10
print("--soal 10--")
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    hasil_jumlah = 0          # untuk menampung hasil penjumlahan 2 elemen
 
    for i in range(n - 2):   # sudah ada 2 elemen awal, loop sisanya
        hasil_jumlah = elem_1 + elem_2   # Proses jumlah
        elem_1 = elem_2                  # Tukar elemen: geser ke kanan
        elem_2 = hasil_jumlah            # Tukar elemen: simpan hasil baru
 
    return hasil_jumlah
 
# test
for i in range(1, 10):
    print(i, "->", fibonacci(i))

#soal 11
print("--soal 11--")
def faktorial_rekursif(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * faktorial_rekursif(n - 1)   # fungsi memanggil dirinya sendiri
 
n = int(input("Masukkan nilai faktorial (rekursif): "))
print(n, "! =", faktorial_rekursif(n))

#soal 12
print("--soal 12--")
def fibonacci_rekursif(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)  # memanggil diri sendiri 2x
 
# test
for i in range(1, 10):
    print(i, "->", fibonacci_rekursif(i))


