# Menyiapkan pesan instruksi untuk pengguna
prompt = "\nMasukkan topping pizza yang kamu inginkan:"
prompt += "\n(Ketik 'quit' jika kamu sudah selesai) "

# Menggunakan while loop untuk meminta input secara berulang
while True:
    topping = input(prompt)
    
    # Cek apakah pengguna ingin berhenti
    if topping.lower() == 'quit':
        print("\nTerima kasih! Pizza kamu sedang disiapkan.")
        break
    else:
        print(f"Menambahkan {topping} ke pizza kamu!")