# 1. Dictionary glossary yang berisi istilah pemrograman (ditambah beberapa istilah baru)
glossary = {
    'dictionary': 'Kumpulan pasangan kunci-nilai (key-value pairs) untuk menyimpan data terkait.',
    'list': 'Kumpulan item yang disusun berurutan dan dapat diubah.',
    'loop': 'Blok kode yang digunakan untuk mengulang suatu tindakan berkali-kali.',
    'string': 'Deretan karakter yang diapit oleh tanda kutip.',
    'if statement': 'Pernyataan bersyarat untuk menjalankan blok kode tertentu jika kondisinya benar.',
    'variable': 'Wadah yang digunakan untuk menyimpan nilai data di dalam memori.',
    'integer': 'Tipe data angka bulat tanpa desimal.',
    'float': 'Tipe data angka yang memiliki titik desimal.',
    'boolean': 'Tipe data yang hanya memiliki dua nilai, yaitu True atau False.',
    'comment': 'Catatan di dalam kode yang diabaikan oleh Python saat program dijalankan.'
}

# 2. Menggunakan for loop untuk mencetak setiap istilah dan artinya secara otomatis
for term, meaning in glossary.items():
    print(f"\nIstilah: {term.title()}")
    print(f"Arti   : {meaning}")