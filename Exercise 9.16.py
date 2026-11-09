from datetime import datetime

# Mendapatkan tanggal dan waktu saat ini secara presisi
waktu_sekarang = datetime.now()
print(f"Waktu dan tanggal sekarang: {waktu_sekarang}")

# Format tanggal agar lebih mudah dibaca (Hari, Tanggal Bulan Tahun)
format_rapi = waktu_sekarang.strftime("%A, %d %B %Y")
print(f"Format tanggal: {format_rapi}")