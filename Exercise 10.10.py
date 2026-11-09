# Nama file teks buku yang ingin dianalisis 
filename = 'alice.txt'

try:
    # Membuka dan membaca isi file teks
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Maaf, file '{filename}' tidak ditemukan.")
else:
    # Menghitung berapa kali kata 'the' muncul (termasuk di dalam kata lain seperti 'then', 'there')
    word_to_count = 'the'
    count_general = contents.lower().count(word_to_count)
    print(f"Kata '{word_to_count}' (secara umum) muncul sebanyak {count_general} kali dalam {filename}.")

    # Menghitung kata 'the ' dengan tambahan spasi di belakangnya 
    # (agar tidak ikut menghitung kata seperti 'then' atau 'there')
    word_precise = 'the '
    count_precise = contents.lower().count(word_precise)
    print(f"Kata '{word_precise}' (dengan spasi) muncul sebanyak {count_precise} kali dalam {filename}.")