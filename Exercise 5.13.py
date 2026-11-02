# Jenis ruangan kelas
print("Selamat datang di Sekolah Python!")
age = int(input("Masukkan usia kamu: "))

if age < 5:
    ruangan_kelas = 0
    print("Ruangan kelas untuk Mars!")
elif age <= 13:
    ruangan_kelas = 1
    print("Anda masuk ke ruangan kelas Jupiter.")
elif age <= 15:
    ruangan_kelas = 2
    print("Anda masuk ke ruangan kelas Saturnus.")
else:
    ruangan_kelas = 3
    print("Anda masuk ke ruangan kelas Uranus.")