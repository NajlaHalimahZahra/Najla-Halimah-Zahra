# Mengembangkan dictionary cities dari Exercise 6.11 dengan menambah informasi baru
cities = {
    'Tokyo': {
        'country': 'Jepang',
        'population': '14 juta jiwa',
        'fact': 'Merupakan salah satu wilayah metropolitan paling padat di dunia.',
        'currency': 'Yen (JPY)',
        'language': 'Jepang'
    },
    'Paris': {
        'country': 'Perancis',
        'population': '2.1 juta jiwa',
        'fact': 'Dikenal sebagai Kota Cinta dan pusat mode dunia.',
        'currency': 'Euro (EUR)',
        'language': 'Perancis'
    },
    'Cairo': {
        'country': 'Mesir',
        'population': '10 juta jiwa',
        'fact': 'Berlokasi dekat dengan kompleks Piramida Giza yang ikonik.',
        'currency': 'Pound Mesir (EGP)',
        'language': 'Arab'
    }
}

# Loop dengan tambahan informasi baru dan format yang lebih elegan
for city_name, city_info in cities.items():
    print(f"\n==============================")
    print(f"KOTA: {city_name.upper()}")
    print(f"==============================")
    print(iklan := f"Negara       : {city_info['country'].title()}")
    print(f"Populasi     : {city_info['population']}")
    print(f"Mata Uang    : {city_info['currency']}")
    print(f"Bahasa Utama : {city_info['language']}")
    print(f"Fakta Unik   : {city_info['fact']}")

print(f"\n==============================")
print("Itu adalah informasi singkat dari kota-kota!")