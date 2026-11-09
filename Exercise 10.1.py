# Nama file yang dibaca
filename = 'learning.txt'

# --- Membaca seluruh file sekaligus ---
print("--- Membaca Seluruh File Sekaligus ---")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.strip())


# --- Membaca dengan meloop baris demi baris ---
print("\n--- Membaca Baris demi Baris dengan For Loop ---")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())


# --- Menyimpan baris ke dalam list menggunakan readlines() ---
print("\n--- Menyimpan ke dalam List menggunakan readlines() ---")
with open(filename) as file_object:
    lines = file_object.readlines()

# Mencetak isi list di luar blok 'with'
for line in lines:
    print(line.strip())