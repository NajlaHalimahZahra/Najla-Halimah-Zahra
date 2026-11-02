# 1. List tempat yang akan didatangi nanti
places = ['Makkah', 'Swiss', 'Palestina', 'Praha', 'Hallstatt', 'Edinburgh']

# 2. Cetak list dalam urutan aslinya
print("Urutan Asli:")
print(places)

# 3. Cetak list dengan sorted() (alfabetis tanpa mengubah list asli)
print("\nUrutan Alfabet (menggunakan sorted()):")
print(sorted(places))

print("\nCek apakah list asli masih utuh:")
print(places)

# 4. Cetak list dengan sorted(reverse=True) (abjad terbalik tanpa mengubah list asli)
print("\nUrutan Abjad Terbalik (sorted dengan reverse):")
print(sorted(places, reverse=True))

print("\nCek lagi apakah list asli masih utuh:")
print(places)

# 5. Gunakan reverse() untuk mengubah urutan list secara permanen
places.reverse()
print("\nList setelah di-reverse (permanen):")
print(places)

# 6. Gunakan reverse() lagi untuk mengembalikan ke urutan semula
places.reverse()
print("\nList dikembalikan ke urutan asli:")
print(places)

# 7. Gunakan sort() untuk mengubah list secara permanen menjadi alfabetis (A-Z)
places.sort()
print("\nList setelah di-sort (A-Z secara permanen):")
print(places)

# 8. Gunakan sort(reverse=True) untuk mengubah list secara permanen menjadi Z-A
places.sort(reverse=True)
print("\nList setelah di-sort reverse (Z-A secara permanen):")
print(places)