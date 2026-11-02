# 1. List tamu sebelumnya (Exercise 3.4)
guest_list = ['Nadia', 'Audia', 'Natha']

print(f"Halo {guest_list[0]}, dateng ya nanti malam.")
print(f"Halo {guest_list[1]}, dateng ya nanti malam.")
print(f"Halo {guest_list[2]}, dateng ya nanti malam.")

# 2. Nama tamu yang tidak bisa hadir 
cant_come = 'Natha'
print(f"\n{cant_come} tidak bisa hadir dalam jamuan makan malam.")

# 3. Mengganti nama tamu yang tidak bisa hadir dengan tamu baru 
# Cari dulu posisi Natha pakai indeks atau langsung ganti elemennya
guest_list[2] = 'Duta'

# 4. Cetak satu set undangan baru untuk semua orang di list
print("\n--- Undangan Baru ---")
print(f"Halo {guest_list[0]}, dateng ya nanti malam.")
print(f"Halo {guest_list[1]}, dateng ya nanti malam.")
print(f"Halo {guest_list[2]}, dateng ya nanti malam.")