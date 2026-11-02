# Input angka dari pengguna dan mengubahnya menjadi integer
number = input("Masukkan sebuah angka, dan akan dilakukan pengecekan apakah itu kelipatan 10: ")
number = int(number)

# Mengecek apakah angka tersebut merupakan kelipatan 10 menggunakan operator modulo
if number % 10 == 0:
    print(f"\nAngka {number} adalah kelipatan 10.")
else:
    print(f"\nAngka {number} BUKAN kelipatan 10.")