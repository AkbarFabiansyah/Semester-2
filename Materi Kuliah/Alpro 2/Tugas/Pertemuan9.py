# # nomor 1

# data = [8, 10, 6, 2, 4]

# for i in range(len(data)):
#     for j in range(0, len(data)-i-1):
#         if data[j] > data[j+1]:
#             data[j], data[j+1] = data[j+1], data[j]

# print(data)

# nomor 2

# data = list(map(int, input("Masukkan angka: ").split()))

# for i in range(len(data)):
#     swapped = False
#     for j in range(0, len(data)-i-1):
#         if data[j] > data[j+1]:
#             data[j], data[j+1] = data[j+1], data[j]
#             swapped = True
#     if not swapped:
#         break

# print("Hasil:", data)

# # nomor 3

# data = [8, 10, 6, 2, 4]
# data.sort()
# print(data)

# #nomor 4
# data = [1, 2, 3, 4, 5]
# data.reverse()
# print(data)

# # nomor 5

# list_1 = [1]
# list_2 = list_1
# list_1[0] = 2

# print(list_2)


# nomor 6
# data = [1, 2, 3, 4, 5]
# print(data[1:4])

# #nomor 7
# data = [1, 2, 3, 4, 5]
# print(data[1:-1])

# #nomor 8
# data = [1, 2, 3, 4, 5]
# print(data[-4:3])

#nomor 9
# data = [1, 2, 3, 4, 5]
# print(data[:3])

# #nomor 10
# data = [1, 2, 3, 4, 5]
# print(data[2:])

#nomor 11
# data = [1, 2, 3]
# copy = data[:]
# print(copy)

# #nomor 12
# data = [1, 2, 3, 4, 5]
# del data[1:3]
# print(data)

#nomor 13
# data = [1, 2, 3]
# del data[:]
# print(data)

# #nomor 14
# data = [1, 2, 3]
# del data
# print(data)

# #nomor 15
# data = [1, 2, 3]
# print(2 in data)

#nomor 16
# data = [1, 2, 3]
# print(5 not in data)

# #nomor 17
# data = [1, 2, 3, 4, 5]
# for i in data:
#     print(i)

# #nomor 18
# data = [1, 2, 3, 4, 5]
# total = sum(data)
# print(total)

# #nomor 19
# data = [1, 2, 3, 4, 5]
# maks = max(data)
# print(maks)

# #nomor 20 : Kuis
# tebakan = [3, 7, 11, 42, 34, 49]
# hasil = [5, 9, 11, 42, 3, 49]

# benar = 0

# for angka in tebakan:
#     if angka in hasil:
#         benar += 1

# print(benar)

#nomor 21  
data = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unik = []

for angka in data:
    if angka not in unik:
        unik.append(angka)

print(unik)


