# Mendefinisikan fungsi make_shirt dengan parameter size dan text
def make_shirt(size, text):
    """Menampilkan ringkasan ukuran dan teks pada kaos."""
    print(f"Membuat kaos ukuran {size.upper()} dengan tulisan: '{text}'")

# Memanggilan pertama menggunakan Positional Arguments
make_shirt('S', 'When the sun goes down, the stars come out')

# Memanggilan kedua menggunakan Keyword Arguments
make_shirt(size='XL', text='ACAB')