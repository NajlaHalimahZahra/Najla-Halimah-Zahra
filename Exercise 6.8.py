# Dictionary untuk hewan peliharaan
pet_1 = {
    'kind': 'kucing',
    'owner': 'Areta'
}

pet_2 = {
    'kind': 'anjing',
    'owner': 'Rosa'
}

pet_3 = {
    'kind': 'kelinci',
    'owner': 'Kiki'
}

# 2. Menyimpan dictionary ke dalam list bernama 'pets'
pets = [pet_1, pet_2, pet_3]

# 3. Loop melalui list pets dan cetak informasinya
for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    
    print(f"Informasi Hewan Peliharaan:")
    print(f"- Jenis hewan : {kind.title()}")
    print(f"- Nama pemilik: {owner.title()}\n")