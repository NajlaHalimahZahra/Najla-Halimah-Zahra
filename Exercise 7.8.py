# Membuat list pesanan dan list kosong untuk sandwich yang sudah jadi
sandwich_orders = ['Tuna', 'Pastrami', 'Grilled Cheese', 'Pepperoni', 'Sausage']
finished_sandwiches = []

# 2. Loop while untuk memproses semua pesanan
while sandwich_orders:
    # Mengambil pesanan pertama dari list menggunakan pop()
    current_sandwich = sandwich_orders.pop(0)
    
    print(f"I made your {current_sandwich} sandwich.")
    
    # Memindahkan sandwich yang sudah dibuat ke list finished_sandwiches
    finished_sandwiches.append(current_sandwich)

# 3. Menampilkan daftar semua sandwich yang sudah selesai dibuat
print("\n--- Daftar Sandwich yang Sudah Selesai ---")
for finished in finished_sandwiches:
    print(f"- {finished.title()} sandwich")