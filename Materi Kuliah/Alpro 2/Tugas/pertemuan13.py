# #nomor 1
# print("Nomor 1")
# tuple_1 = (1, 2, 3)
# tuple_2 = 1, 2, 3

# print(tuple_1)
# print(tuple_2)

# #nomor 2
# print("\nNomor 2")
# my_tuple =(1, 10, 100, 1000)

# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])

# for element in my_tuple:
#     print(element)

# #nomor 3
# print("\nNomor 3")
# my_tuple =(1, 10, 100, 1000)

# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10

# print(my_tuple)

# #nomor 4
# print("\nNomor 4")
# my_tuple = (1, 10, 100, 1000)
# t1 = my_tuple + (10000, 100000)
# t2 = my_tuple * 3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

# #nomor 5
# print("\nNomor 5")
# x, y = 1, 2

# var= 123
# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)
# t1, t2, t3= t2, t3, t1
# print(t1, t2, t3)

# #nomor 6
# print("\nNomor 6")
# dictionary = {"cat": "meong", "dog": "anjing", "horse": "kuda"}
# nilai_alpro2 = {"rusdi": 60, "mas gatot": 80, "mas amba": 90}
# dictionary_kosong = {}

# print(dictionary)
# print(nilai_alpro2)
# print(dictionary_kosong)

# #nomor 7
# print("\nNomor 7")
# dictionary = {"cat": "meong", "dog": "anjing", "horse": "kuda"}
# nilai_alpro2 = {"rusdi": 60, "mas gatot": 80, "mas amba": 90}
# dictionary_kosong = {}

# print(dictionary["cat"])
# print(nilai_alpro2["mas amba"])

# #nomor 8
# print("\nNomor 8")
# dictionary = {"cat": "meong", "dog": "anjing", "horse": "kuda"}
# for key in dictionary.keys():
#     print(key, "-->", dictionary[key])

# #nomor 9
# print("\nNomor 9")
# dictionary = {"cat": "meong", "dog": "anjing", "horse": "kuda"}
# for value in dictionary.values():
#     print(value)

# #nomor 10
# print("\nNomor 10")
# dictionary = {"cat": "meong", "dog": "anjing", "horse": "kuda"}
# for uhuy, item in dictionary.items():
#     print(uhuy,"-->", item)

# #nomor 11
# print("\nNomor 11")
# dictionary = {"cat": "meong", "dog": "anjing", "horse": "kuda"}
# dictionary.update({"monkey": "monyet"})

# print(dictionary)

# #nomor 12
# print("\nNomor 12")
# dictionary = {"cat": "meong", "dog": "anjing", "horse": "kuda"}
# dictionary.popitem()
# print(dictionary)

# #nomor 13
# print("\nNomor 13")
# dictionary = {"cat": "meong", "dog": "anjing", "horse": "kuda"}
# dictionary["cat"] = "gustavo fring"
# print(dictionary)

# dictionary["horse"] = "kuda nil"
# print(dictionary)

# del dictionary["dog"]
# print(dictionary)

# #nomor 14
# print("\nNomor 14")
# kelas_informatika = {}

# while True:
#     nama = input("Masukkan nama mahasiswa: ")
#     if nama == "":
#         break

#     try:
#         nilai = int(input("Masukkan nilai (0-10): "))
#         if nilai not in range(0, 11):
#             print("Nilai harus 0-10!")
#             continue
#     except:
#         print("Input nilai harus angka!")
#         continue

#     if nama in kelas_informatika:
#         kelas_informatika[nama] += (nilai,)
#     else:
#         kelas_informatika[nama] = (nilai,)

# for nama in sorted(kelas_informatika.keys()):
#     total = sum(kelas_informatika[nama])
#     jumlah = len(kelas_informatika[nama])
#     print(nama, ":", total / jumlah)

#nomor 15
print("\nNomor 15")
kelas_informatika = {}

while True:
    try:
        nama = input("Masukkan nama mahasiswa: ")
        if nama == "":
            break

        nilai = int(input("Masukkan nilai (0-10): "))
        if nilai not in range(0, 11):
            raise ValueError

    except ValueError:
        print("Nilai harus angka antara 0 sampai 10!")
        continue
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user")
        break
    except Exception as e:
        print("Terjadi error lain:", e)
        continue

    if nama in kelas_informatika:
        kelas_informatika[nama] += (nilai,)
    else:
        kelas_informatika[nama] = (nilai,)

for nama in sorted(kelas_informatika.keys()):
    total = sum(kelas_informatika[nama])
    jumlah = len(kelas_informatika[nama])
    print(nama, ":", total / jumlah)


