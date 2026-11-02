# 1. List tamu sebelumnya (Exercise 3.4)
guest_list = ['Nadia', 'Audia', 'Natha']

print("Halo semuanya, jadi kita akan pindah lokasi karena mendapatkan tempat yang lebih luas")

# 2. Menambahkan tamu baru di awal list menggunakan insert()
guest_list.insert(0, 'Nora')

# 3. Menambahkan tamu baru di tengah list menggunakan insert()
# Menghitung posisi tengah secara manual (indeks ke-2)
guest_list.insert(2, 'Jia')

# 4. Menambahkan tamu baru di akhir list menggunakan append()
guest_list.append('Ayesha')

# 5. Nama tamu yang tidak bisa hadir 
cant_come = 'Natha'
print(f"\n{cant_come} tidak bisa hadir dalam jamuan makan malam.")

# 6. Mengganti nama tamu yang tidak bisa hadir dengan tamu baru 
# Cari dulu posisi Natha pakai indeks atau langsung ganti elemennya
guest_list[4] = 'Duta'

# 7. Cetak satu set undangan baru untuk semua orang di list
print("\n--- Undangan Baru Tambahan Tamu ---")
print(f"Halo {guest_list[0]}, dateng ya nanti malam.")
print(f"Halo {guest_list[1]}, dateng ya nanti malam.")
print(f"Halo {guest_list[2]}, dateng ya nanti malam.")
print(f"Halo {guest_list[3]}, dateng ya nanti malam.")
print(f"Halo {guest_list[4]}, dateng ya nanti malam.")
print(f"Halo {guest_list[5]}, dateng ya nanti malam.")