# Mendefinisikan fungsi make_shirt dengan nilai default untuk size dan text
def make_shirt(size='medium', text='The achievers'):
    """Menampilkan ringkasan ukuran dan teks pada kaos."""
    print(f"Membuat kaos ukuran {size.upper()} dengan tulisan: '{text}'")

# Membuat kaos ukuran Large dengan pesan default
make_shirt()

# Membuat kaos ukuran Large dengan pesan default
make_shirt(size='large')

# Membuat kaos dengan ukuran dan pesan yang berbeda 
make_shirt(size='small', text='Back to December')