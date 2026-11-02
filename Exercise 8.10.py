# Membuat list awal berisi pesan-pesan singkat
text_messages = [
    "Halo, apa kabar?", 
    "Jangan lupa pakai jaket kalau malam.", 
    "Besok jadi kerja kelompok?", 
    "Semangat ya!"
]

sent_messages = []

# Mendefinisikan fungsi send_messages
def send_messages(messages, sent):
    """Mencetak setiap pesan dan memindahkannya ke list sent_messages."""
    print("--- MEMPROSES PENGIRIMAN PESAN ---")
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: '{current_message}'")
        sent.append(current_message)

# Memanggil fungsi dengan mengirimkan SALINAN list (menggunakan [:])
send_messages(text_messages[:], sent_messages)

# Menampilkan kedua list untuk memeriksa hasilnya
print("\n--- STATUS AKHIR ---")
print(f"List Asli (text_messages): {text_messages}")
print(f"List Terkirim (sent_messages): {sent_messages}")