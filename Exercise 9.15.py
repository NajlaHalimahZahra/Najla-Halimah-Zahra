from random import choice

def make_random_ticket(pool):
    """Fungsi pembantu untuk membuat 1 tiket acak berisi 4 elemen unik."""
    ticket = []
    while len(ticket) < 4:
        item = choice(pool)
        if item not in ticket:
            ticket.append(item)
    return ticket

# Kumpulan data (pool) 
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Tentukan tiket pribadi (my_ticket)
my_ticket = [4, 7, 'a', 'e']  # Bisa diubah

print(f"Tiket saya: {my_ticket}")
print("Memulai simulasi pencarian pemenang undian...")

# Simulasi loop sampai tiket menang cocok dengan my_ticket
winning_ticket = []
loop_count = 0

while winning_ticket != my_ticket:
    winning_ticket = make_random_ticket(lottery_pool)
    loop_count += 1
    
    # Opsional: Cetak progres setiap 10.000 percobaan 
    if loop_count % 100 == 0:
        print(f"Percobaan ke-{loop_count}: Belum tembus (Hasil undian: {winning_ticket})")

# Hasil akhir ketika menang
print("\n--- SELAMAT! ANDA MENANG! ---")
print(f"Tiket pemenang yang keluar: {winning_ticket}")
print(f"Total percobaan yang dibutuhkan sampai menang: {loop_count:,} kali undian.")