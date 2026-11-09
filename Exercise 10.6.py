print("=== PROGRAM PENJUMLAHAN DUA ANGKA ===")

# Input angka pertama dan kedua
first_number = input("\nMasukkan angka pertama: ")
second_number = input("Masukkan angka kedua: ")

try:
    # Mengubah input string menjadi integer lalu menjumlahkannya
    sum_result = int(first_number) + int(second_number)
except ValueError:
    # Blok akan tereksekusi jika pengguna memasukkan huruf/teks
    print("Maaf, Anda memasukkan teks/huruf, bukan angka yang valid!")
else:
    # Blok berjalan jika tidak ada error sama sekali
    print(f"Hasil penjumlahan dari {first_number} + {second_number} adalah: {sum_result}")