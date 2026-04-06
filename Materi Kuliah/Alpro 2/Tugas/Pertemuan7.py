#soal 1
my_list = [10, 20, 30, 40, 50]
print(my_list[0])
print(my_list[2])

#soal 2
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print(item)

#soal 3
data = [1, 2, 3, 4, 5]
print(len(data))

#soal 4
angka = [1, 2, 3, 4]
angka.remove(3)
print(angka)

#soal 5
data = [10, 20, 30, 40]
print(data[-1])
print(data[-2])

#soal 6
topi_list = [1, 2, 3, 4, 5]  # Angka yang tersembunyi di dalam topi pesulap

# Langkah 1: input untuk mengganti nilai tengah
topi_list[len(topi_list)//2] = int(input("Masukkan angka: "))

# Langkah 2: hapus elemen terakhir
topi_list.pop()

# Langkah 3: tampilkan panjang list
print(len(topi_list))

print(topi_list)

#soal 7
angka = [111, 7, 2, 1]
print(len(angka))
print(angka)

###

angka.append(4)

print(len(angka))
print(angka)

###

angka.insert(0, 222)
print(len(angka))
print(angka)

# Tambahkan nilai 333 pada index ke-1
angka.insert(1, 333)

# Print panjang listnya
print(len(angka))

# Print isi listnya
print(angka)

#soal 8
my_list = [] # membuat list kosong

# Mengisi list dengan append yang berulang
for i in range(5):
    my_list.append(i + 1)

print(my_list)

#soal 9
my_list = [] # membuat lsit kosong

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

#soal 10
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#soal 11
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

#soal 12
my_list = [10, 1, 8, 3, 5]

# Menukar elemen ujung ke ujung secara manual
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# yang menggunakan for

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

# Melakukan perulangan hanya sampai setengah panjang list (length // 2)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

#soal 13

# Langkah 1: Buatlah sebuah list kosong dengan nama exo
exo = []
print("Langkah 1: ", exo)

# Langkah 2: Gunakan method append() untuk menambahkan anggota: Suho, Kai, Chanyeol dan Sehun
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2: ", exo)

# Langkah 3: Gunakan for untuk menambahkan anggota: DO, Baekhyun, Kris, Lay, Luhan, Tao, dan Chen
tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for anggota in tambahan:
    exo.append(anggota)
print("Langkah 3: ", exo)

# Langkah 4: Hapuslah anggota: Kris, Luhan dan Tao
# Menggunakan method remove()
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print("Langkah 4: ", exo)

# Langkah 5: Gunakan method insert() untuk menambahkan anggota Xiumin pada elemen ke tiga dari terakhir
# "Ke tiga dari terakhir" dalam Python indexing adalah -3
exo.insert(-2, "Xiumin") 
print("Langkah 5: ", exo)

print("Jumlah anggota exo: ", len(exo))
