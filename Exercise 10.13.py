import json

filename = 'user_profile.json'

try:
    
    with open(filename, 'r') as f:
        user_profile = json.load(f)
        print(f"Selamat datang kembali, {user_profile['username']}!")
        print("Berikut informasi profil yang saya ingat tentang Anda:")
        for key, value in user_profile.items():
            print(f"- {key.title()}: {value}")

except FileNotFoundError:
    # Jika file belum ada, kumpulkan beberapa informasi dalam bentuk dictionary
    user_profile = {}
    
    user_profile['username'] = input("Siapa nama pengguna (username) Anda? ")
    user_profile['age'] = input("Berapa usia Anda? ")
    user_profile['hobby'] = input("Apa hobi utama Anda? ")

    # Simpan dictionary ke dalam file JSON
    with open(filename, 'w') as f:
        json.dump(user_profile, f)
        print("\nTerima kasih! Profil lengkap Anda telah berhasil disimpan.")