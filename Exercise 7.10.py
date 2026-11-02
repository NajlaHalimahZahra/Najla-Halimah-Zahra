# Dictionary kosong untuk menampung hasil polling
responses = {}

# Mengatur flag untuk mengontrol perulangan while
polling_active = True

while polling_active:
    # Meminta nama dan destinasi liburan impian dari pengguna
    print("\n--- Survei Liburan Impian ---")
    name = input("Siapa nama kamu? ")
    response = input("Jika kamu bisa mengunjungi satu tempat di dunia, kamu ingin pergi ke mana? ")
    
    # Menyimpan jawaban ke dalam dictionary
    responses[name] = response
    
    # Menanyakan apakah ada orang lain yang ingin ikut mengisi survei
    repeat = input("Apakah ada orang lain yang ingin ikut mengisi survei? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# 3. Menampilkan hasil keseluruhan polling setelah selesai
print("\n--- HASIL POLL: LIBURAN IMPIAN ---")
for name, place in responses.items():
    print(f"{name.title()} ingin sekali berkunjung ke {place.title()}.")