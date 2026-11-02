# 3 dictionary berbeda untuk mewakili tiga orang
person_1 = {
    'first_name': 'Mikasa',
    'last_name': 'Ackerman',
    'age': 19,
    'city': 'Jakarta Selatan'
}

person_2 = {
    'first_name': 'Katarina',
    'last_name': 'Blue',
    'age': 26,
    'city': 'Surabaya'
}

person_3 = {
    'first_name': 'Hazel',
    'last_name': 'Renjana',
    'age': 17,
    'city': 'Semarang'
}

# Simpan dictionary ke dalam list bernama 'people'
people = [person_1, person_2, person_3]

# Loop melalui list people dan cetak informasi setiap orang
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    
    print(f"Nama : {full_name.title()}")
    print(f"Umur : {age} tahun")
    print(f"Kota : {city}\n")