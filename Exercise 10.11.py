import json

# --- Simpan Angka Favorit ke File JSON ---
filename = 'favorite_number.json'

# Meminta input angka favorit dari pengguna
favorite_number = input("Berapa angka favoritmu? ")

# Menyimpan angka tersebut ke dalam file menggunakan json.dumps() / json.dump()
with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    print(f"Terima kasih! Angka favorit {favorite_number} telah disimpan.")


# --- Membaca Kembali Angka dari File JSON ---
try:
    with open(filename, 'r') as f:
        number = json.load(f)
        print(f"Saya tahu angka favoritmu! Angkanya adalah {number}.")
except FileNotFoundError:
    print("File data tidak ditemukan.")