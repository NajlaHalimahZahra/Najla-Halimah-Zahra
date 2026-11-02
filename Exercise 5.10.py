current_users = ["admin", "Luna", "Jovan", "Kinara", "Sagara"]
new_users = ["ADMIN", "LUNA", "Baila", "Orel", "Giana"]

# List baru yang berisi versi huruf kecil dari current_users
# Supaya pengecekan tidak terhalang oleh perbedaan huruf besar/kecil
current_users_lower = [user.lower() for user in current_users]

# 3. Loop untuk memeriksa setiap new_user
for new_user in new_users:
    # Apakah versi huruf kecil dari new_user ada di dalam current_users_lower
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' sudah terpakai. Silakan masukkan username lain.")
    else:
        print(f"Username '{new_user}' tersedia!")