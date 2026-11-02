# Meminta input jumlah orang dan mengubahnya menjadi integer
party_size = input("How many people are in your dinner group tonight? ")
party_size = int(party_size)

# Mengecek ketersediaan meja berdasarkan jumlah orang
if party_size > 8:
    print("\nSorry, you'll have to wait for a table.")
else:
    print("\nYour table is ready!")