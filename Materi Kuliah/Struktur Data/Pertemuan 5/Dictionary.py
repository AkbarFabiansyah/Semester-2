#membuat struktur data dictionary
userlogin ={"name":"Akbar Fabiansyah","age":19, "Role":"Cyber Security"}
print(type(userlogin));

#mengakses data dalam dictionary
print(f"Nama Akun : {userlogin['name']}")
print(f"Umur Akun : {userlogin['age']} tahun")
print(f"Role Akun : {userlogin['Role']}")

#akses data seluruh
print(userlogin.items())
print(userlogin.keys())
print(userlogin.values())

#menambahkan data baru dalam dictionary
userlogin["email"] = "AkbarFabiansyah@gmail.com"
print(userlogin)

#menghapus data big_On dari dictionary
userlogin.pop("email")
print(userlogin)

#mengubah data kedalam dictionari big-O 0(1)
userlogin["name"] = "user"
print(userlogin)

#nested dictionary
dbUser = {"user1":{"name":"Akbar","age":19, "Role":"data analyst"},
"user2":{"name":"Ucok","age":25, "Role":"Backend Developer"},
"user3":{"name":"Joni","age":20, "Role":"frontend Developer"}}

print(dbUser)
#akses value base key
print(dbUser["user1"])

#melakukan pencarian data dalam dictionary
findword =  input("Masukkan Kata yang ingin dicari : ")
if findword in dbUser:
    print("Data ditemukan")
    print(dbUser[findword])
else: 
    print("Data tidak ditemukan")