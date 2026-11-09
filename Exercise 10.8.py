# Daftar file dibaca oleh program
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\n--- Membaca file: {filename} ---")
    
    try:
        # Buka dan baca isi file
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents.strip())
            
    except FileNotFoundError:
        # Pesan jika file tidak ditemukan
        print(f"Maaf, file '{filename}' tidak ditemukan di direktori ini.")