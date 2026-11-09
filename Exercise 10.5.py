# Nama file buku tamu
filename = 'guest_book.txt'

print("=== BUKU TAMU DIGITAL ===")
print("Ketik 'quit' jika sudah selesai.")

while True:
    name = input("\nMasukkan nama Anda: ")
    
    # Kondisi untuk menghentikan perulangan
    if name.lower() == 'quit':
        print("Terima kasih! Buku tamu telah ditutup.")
        break
        
    # Membuka file dalam mode append ('a') agar data lama tidak terhapus
    with open(filename, 'a') as file_object:
        # Menulis nama tamu diikuti dengan baris baru (\n)
        file_object.write(f"{name}\n")
        
    print(f"Selamat datang, {name}! Nama Anda telah dicatat di buku tamu.")