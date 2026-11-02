# Membuat list yang berisi beberapa pesan singkat
text_messages = [
    "Halo, apa kabar?", 
    "Jangan lupa pakai jaket kalau malam.", 
    "Besok jadi kerja kelompok?", 
    "Semangat ya!"
]

# Mendefinisikan fungsi show_messages dengan parameter list
def show_messages(messages):
    """Menampilkan setiap pesan di dalam list."""
    print("--- DAFTAR PESAN ---")
    for message in messages:
        print(message)

# Memanggil fungsi dengan mengirimkan list text_messages
show_messages(text_messages)