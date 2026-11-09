# Nama file tempat menyimpan nama tamu
filename = 'guest.txt'

# Input nama dari pengguna
guest_name = siapa_namamu = input("Masukkan nama Anda: ")

# Buka file dalam mode write ('w') dan menuliskan nama ke dalamnya
with open(filename, 'w') as file_object:
    file_object.write(guest_name)
    
print(f"Terima kasih! Nama '{guest_name}' telah disimpan ke dalam file {filename}.")