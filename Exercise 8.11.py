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
    while messages:
        current_message = messages.pop(0)
        sent.append(current_message)

# Memanggil fungsi dengan SALINAN list menggunakan slice [:] 
# Membuat list baru untuk menampung hasil kirim latihan ini
sent_messages_archived = []
send_messages(text_messages[:], sent_messages_archived)

print("--- HASIL SETELAH MENGGUNAKAN SALINAN ([:] ) ---")
print(f"List Asli (text_messages) tetap utuh: {text_messages}")
print(f"List Terkirim (sent_messages_archived): {sent_messages_archived}")


# CONTOH JIKA TANPA SALINAN (Mengirim list asli langsung)
# text_messages asli akan dikosongkan oleh fungsi .pop() di dalam fungsi
print("\n--- HASIL JIKA MENGIRIM LIST ASLI TANPA SALINAN ---")
send_messages(text_messages, sent_messages)
print(f"List Asli (text_messages) sekarang kosong: {text_messages}")
print(f"List Terkirim (sent_messages): {sent_messages}")