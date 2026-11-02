# Menyiapkan pesan instruksi untuk pengguna
prompt = "\nMasukkan usia kamu:"
prompt += "\n(Ketik 'quit' jika sudah selesai) "

# Menggunakan while loop untuk menghitung harga tiket secara berulang
while True:
    age = input(prompt)
    
    # Cek apakah pengguna ingin keluar
    if age.lower() == 'quit':
        print("\nTerima kasih! Selamat menikmati filmnya.")
        break
        
    # Ubah input usia menjadi integer
    age = int(age)
    
    # Menentukan harga tiket berdasarkan ketentuan usia
    if age < 3:
        print("Tiket kamu GRATIS!")
    elif age <= 12:
        print("Harga tiket kamu adalah $10.")
    else:
        print("Harga tiket kamu adalah $15.")