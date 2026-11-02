# 1. Membuat list awal berisi judul lagu
songs_name = ["That's What You Get", "Quit", "Roslyn", "The Number 1 Party Anthem", "White Mustang"]
print("List Awal:")
print(songs_name)

# 2. Menggunakan len() untuk menghitung jumlah item
print(f"\nJumlah lagu dalam list: {len(songs_name)}")

# 3. Mengakses elemen menggunakan indeks
print(f"\nLagu pertama di list adalah {songs_name[0]}")

# 4. Mengubah elemen di dalam list (indeks ke-1 diubah dari 'That's What You Get' jadi 'Ain't It Fun')
songs_name[0] = "Ain't It Fun"
print("\nSetelah mengubah elemen (That's What You Get jadi Ain't It Fun):")
print(songs_name)

# 5. Menambahkan elemen di akhir menggunakan append()
songs_name.append('Roxanne')
print("\nSetelah append ('Roxanne'):")
print(songs_name)

# 6. Menambahkan elemen di posisi tertentu menggunakan insert()
songs_name.insert(2, 'Fluroescence Adolescence')
print("\nSetelah insert ('Fluroescence Adolescence' di indeks 2):")
print(songs_name)

# 7. Menghapus elemen menggunakan del (menghapus item pertama)
del songs_name[0]
print("\nSetelah del elemen pertama:")
print(songs_name)

# 8. Menghapus elemen menggunakan pop() (menghapus item terakhir dan menyimpannya)
popped_song = songs_name.pop()
print(f"\nLagu yang dihapus dari list: {popped_song}")
print("List setelah pop:")
print(songs_name)

# 9. Menghapus elemen berdasarkan nilai menggunakan remove()
songs_name.remove('Fluroescence Adolescence')
print("\nSetelah remove ('Fluroescence Adolescence'):")
print(songs_name)

# 10. Menggunakan sorted() untuk mengurutkan sementara (A-Z)
print("\nMenggunakan sorted (sementara A-Z):")
print(sorted(songs_name))
print("\nList asli tetap tidak berubah:")
print(songs_name)

# 11. Menggunakan reverse() untuk membalikkan urutan secara permanen
songs_name.reverse()
print("\nSetelah reverse (permanen dibalik):")
print(songs_name)

# 12. Menggunakan sort() untuk mengurutkan secara permanen (A-Z)
songs_name.sort()
print("\nSetelah sort (permanen A-Z):")
print(songs_name)

# 13. Menggunakan sort(reverse=True) untuk mengurutkan permanen (Z-A)
songs_name.sort(reverse=True)
print("\nSetelah sort, (permanen Z-A):")
print(songs_name)