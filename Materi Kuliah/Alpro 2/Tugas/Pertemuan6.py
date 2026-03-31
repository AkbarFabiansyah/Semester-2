#Soal 1
#while True:
#print("nyangkut di perulangan tak terhingga")

#soal 2
#contoh 2
counter = 5
while counter > 2:
    print(counter)
    counter -=1

#soal 3
#membuat variabel angka ganjil dan angka genap
angka_genap = 0
angka_ganjil = 0

#membaca angka pertama
angka = int(input("masukkan suatu angka atau ketik angka 0 untuk berhenti: "))
while angka != 0: #cek apakah angka tidak sama dengan 0

    if angka % 2 == 1: #mengecek apakah sisa bagi angka dengan 2 adalah 1
        angka_ganjil += 1
    else:
        angka_genap += 1

#membaca angka selanjutnya
angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))
#menampilkan total angka ganjil dan angka genap
print("jumlah angka Ganjil: ", angka_ganjil)
print("jumlah angka Genap: ", angka_genap)

#soal 4
secret_number = 777
print(
"""
+======================================+
| Selamat datang di game saya, muggle! |
| masukkan suatu angka dan tebak |
| angka berapa yang saya pilih |
| untuk kamu. |
| Jadi, berapa angka rahasianya? |
+======================================+
""")

# Lanjutkan kode disini
while True:
    angka = int(input("Masukkan angka: "))
    if angka == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break
    else:
        print("hahaha ! kamu nyangkut deh di Loop saya")

#soal 5
for a in range(10):
    print("nilai a saat ini adalah", a)
for b in range(2,8):
    print("nilai b saat ini adalah", b)
for c in range(2,8,3):
    print("nilai c saat ini adalah", c)
for d in range(1,1):
    print("nilai d saat ini adalah", d)
for e in range(2,1):
    print("nilai e saat ini adalah", e)

#soal 6
power = 1
for expo in range(11):
    print (("2 pangkat"), expo, "adalah ", power)
    power *=2

#soal 7
#contoh break
print("Intruksi break:")
for i in range (1,6):
    if i == 3:
        break
    print("bagian ini ada di dalam loop.", i)
print("bagian ini ada d luar loop.")

#contoh continue
print("\nInstruksi continue :")
for i in range (1,6):
    if i == 3:
        continue
    print("bagian ini ada di dalam loop.", i)
print("bagian ini ada d luar loop.")

#soal 8
secret_number = 777
print("""
+====================================+
| Selamat datang di game saya, Muggle! |
| Masukkan suatu angka dan tebak |
| angka berapa yang saya pilih untukmu|
| Jadi, berapa angka rahasianya? |
+====================================+
""")
while True:
    guess = int(input("Masukkan angka tebakanmu: "))
    if guess == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break
    else:
        print("hahaha! kamu nyangkut deh di Loop saya")

#soal 9

# meminta user memasukkan suatu kata
# simpan kata tersebut ke variabel user_word
user_word = input("Masukkan sebuah kata: ")
# ubah ke huruf kapital

user_word = user_word.upper()   

for kata in user_word:
    # cek apakah huruf vokal
    if kata == "A":
        continue
    elif kata == "I":
        continue
    elif kata == "U":
        continue
    elif kata == "E":
        continue
    elif kata == "O":
        continue
    else:
        print(kata)

#soal 10
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#soal 11
for i in range(5):
    print(i)
else:
    print("else:", i)

#soal 12

# operasi logical
a = True
b = False
print(a and b)

#soal 13

# operasi logical
a = True
b = False
print(a and b)

# operasi bit
x = 5
y = 3
print(x & y)

var = 17
var_right = var >> 1
Var_left = var << 2
print(var, var_right, Var_left)

#soal 14
var = 17
var_right = var >> 1
Var_left = var << 2
print(var, var_right, Var_left)

#soal 15
x = 4
y = 1
a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2
print(a, b, c, d, e, f)