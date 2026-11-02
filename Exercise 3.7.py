# 1. Mulai dari program Exercise 3.6 (List berisi 6 tamu)
guest_list = ['Nora', 'Nadia', 'Duta', 'Audia', 'Jia', 'Ayesha']

# Menginformasikan bahwa meja baru tidak datang tepat waktu
print("Maaf ya, ada kesalahan data reservasi, jadi aku hanya bisa mengundang dua orang.")

# 2. Mengeluarkan tamu satu per satu menggunakan pop()
# Mengeluarkan tamu terakhir sampai tersisa 2 orang
popped_guest = guest_list.pop()
print(f"Maaf ya {popped_guest}, kamu tidak bisa diundang karena keterbatasan tempat.")

popped_guest = guest_list.pop()
print(f"Maaf ya {popped_guest}, kamu tidak bisa diundang karena keterbatasan tempat.")

popped_guest = guest_list.pop()
print(f"Maaf ya {popped_guest}, kamu tidak bisa diundang karena keterbatasan tempat.")

popped_guest = guest_list.pop()
print(f"Maaf ya {popped_guest}, kamu tidak bisa diundang karena keterbatasan tempat.")

# 3. Mencetak pesan untuk dua orang yang masih tersisa di list
print(f"\nHalo {guest_list[0]}, kamu masih tetap diundang!")
print(f"Halo {guest_list[1]}, kamu masih tetap diundang!")

# 4. Menggunakan del untuk menghapus dua nama terakhir dari list
del guest_list[0]
del guest_list[0] # Indeks 0 lagi karena elemen sebelumnya sudah terhapus

# 5. Mencetak list untuk memastikan sudah kosong
print("\nIsi list akhir:", guest_list)