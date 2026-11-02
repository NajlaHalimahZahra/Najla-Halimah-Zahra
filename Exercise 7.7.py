# CONTOH INFINITE LOOP (Perulangan Tanpa Henti)
# Cara menghentikannya di terminal: Tekan tombol Ctrl + C

x = 1
while x <= 5:
    print(f"Angka saat ini: {x}")
    # Sengaja TIDAK menuliskan 'x += 1' agar nilai x tidak pernah bertambah,
    # sehingga kondisi 'x <= 5' akan SELALU True selamanya!