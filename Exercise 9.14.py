from random import choice

# Membuat list/tuple berisi 10 angka dan 5 huruf
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Mengambil 4 item secara acak untuk dijadikan pemenang undian
winning_ticket = []

# Loop 4 kali untuk mengambil 4 item unik, atau langsung pilih 4 kali
while len(winning_ticket) < 4:
    selected_item = choice(lottery_pool)
    
    # Pastikan item belum ada di dalam winning_ticket supaya tidak kembar
    if selected_item not in winning_ticket:
        winning_ticket.append(selected_item)

# Cetak hasil undian ke layar
print("--- PENGUNDIAN LOTRE ---")
print(f"Kombinasi tiket pemenang yang ditarik adalah: {winning_ticket}")
print("Pesan: Tiket apa pun yang mencocokkan 7 angka atau huruf ini memenangkan hadiah utama!")