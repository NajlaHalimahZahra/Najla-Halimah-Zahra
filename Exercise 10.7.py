print("=== KALKULATOR PENJUMLAHAN (KETIK 'q' UNTUK KELUAR) ===")

while True:
    # Input angka pertama
    first_number = input("\nMasukkan angka pertama: ")
    if first_number.lower() == 'q':
        print("Terima kasih telah menggunakan kalkulator!")
        break
        
    # Input angka kedua
    second_number = input("Masukkan angka kedua: ")
    if second_number.lower() == 'q':
        print("Terima kasih telah menggunakan kalkulator!")
        break

    try:
        # Mengubah input menjadi angka dan menjumlahkannya
        sum_result = int(first_number) + int(second_number)
    except ValueError:
        # Jika user memasukkan huruf, beri tahu dan ulangi dari awal loop
        print("Oops! Harap masukkan angka yang valid, bukan teks/huruf.")
    else:
        # Jika berhasil tanpa error, tampilkan hasil
        print(f"Hasil penjumlahan: {first_number} + {second_number} = {sum_result}")