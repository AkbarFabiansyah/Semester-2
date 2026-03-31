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
