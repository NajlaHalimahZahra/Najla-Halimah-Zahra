# File yang ingin dibaca
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\n--- Mencoba membaca file: {filename} ---")
    
    try:
        # Buka dan baca isi file
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents.strip())
            
    except FileNotFoundError:
        # Gagal secara diam-diam menggunakan 'pass'
        pass