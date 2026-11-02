# Mendefinisikan fungsi make_album dengan parameter opsional jumlah lagu (tracks)
def make_album(artist_name, album_title, tracks=None):
    """Membangun dictionary yang mendeskripsikan sebuah album musik."""
    album = {
        'artist': artist_name,
        'title': album_title
    }
    
    # Jika parameter tracks diisi, tambahkan ke dalam dictionary
    if tracks:
        album['num_tracks'] = tracks
        
    return album

# 2. Memanggil fungsi untuk tiga album berbeda
album_1 = make_album('Paramore', 'Riot')
album_2 = make_album('Artic Monkeys', 'AM')
album_3 = make_album('Lana Del Rey', 'Ultraviolence', tracks=8) # Menggunakan parameter opsional

# 3. Mencetak hasil dictionary
print(album_1)
print(album_2)
print(album_3)