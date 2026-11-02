# 1. Membuat list pesanan dan list kosong untuk sandwich yang sudah jadi
sandwich_orders = ['Tuna', 'Pastrami', 'Grilled Cheese', 'Pepperoni', 'Sausage']
finished_sandwiches = []

print("--- DAFTAR PESANAN AWAL ---")
print(sandwich_orders)

# 2. Mengumumkan bahwa deli kehabisan pastrami
print("\nMaaf, deli sedang kehabisan pastrami!")

# 3. Menggunakan while loop untuk menghapus semua kemunculan 'pastrami'
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# 4. Menampilkan daftar pesanan setelah dibersihkan
print("\n--- DAFTAR PESANAN SETELAH PASTRAMI DIHAPUS ---")
print(sandwich_orders)