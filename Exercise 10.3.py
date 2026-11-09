# Nama file yang dibaca
filename = 'learning.txt'

print("--- Menggunakan splitlines() agar kode lebih ringkas ---")

with open(filename) as file_object:
    # Membaca seluruh isi file sekaligus, mengubah list per baris dengan splitlines()
    lines = file_object.read().splitlines()

# Melakukan looping langsung dari list hasil splitlines()
for line in lines:
    print(line.strip())