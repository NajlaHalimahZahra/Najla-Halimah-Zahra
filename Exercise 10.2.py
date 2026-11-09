# Nama file yang dibaca
filename = 'learning.txt'

print("--- Membaca dan Mengubah Kata ---")

with open(filename) as file_object:
    for line in file_object:
        # Mengganti kata 
        modified_line = line.replace("I've never expected", "I'm glad")
        
        # Mencetak hasil modifikasi ke layar (strip() untuk merapikan spasi/enter berlebih)
        print(modified_line.strip())
