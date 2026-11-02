# Fungsi make_album dari latihan sebelumnya
def make_album(artist_name, album_title, tracks=None):
    """Membangun dictionary yang mendeskripsikan sebuah album musik."""
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if tracks:
        album['num_tracks'] = tracks
    return album

# While loop untuk input interaktif dari pengguna
print("--- Program Koleksi Album Musik ---")
print("(Ketik 'quit' kapan saja untuk keluar)\n")

while True:
    artist = input("Masukkan nama artis: ")
    if artist.lower() == 'quit':
        break
        
    title = input("Masukkan judul album: ")
    if title.lower() == 'quit':
        break
        
    # Memanggil fungsi make_album dan mencetak hasilnya
    album_info = make_album(artist, title)
    print("\nAlbum yang berhasil dibuat:")
    print(album_info)
    print("-" * 35)

print("\nTerima kasih telah menggunakan program ini!")