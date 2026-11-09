import json

# Tentukan nama file tempat menyimpan angka favorit
filename = 'favorite_number.json'

try:
    # Coba buka dan baca isi file JSON
    with open(filename, 'r') as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    # Jika file belum ada, minta input dari pengguna
    favorite_number = input("Berapa angka favoritmu? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
        print(f"Terima kasih! Angka favorit {favorite_number} telah disimpan.")
else:
    # Jika file berhasil dibaca, tampilkan hasilnya
    print(f"Angka favoritmu adalah {favorite_number}.")