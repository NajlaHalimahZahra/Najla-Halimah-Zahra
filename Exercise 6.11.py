# Dictionary bersarang untuk menyimpan data kota
cities = {
    'Tokyo': {
        'country': 'Jepang',
        'population': '14 juta jiwa',
        'fact': 'Merupakan salah satu wilayah metropolitan paling padat di dunia.'
    },
    'Paris': {
        'country': 'Perancis',
        'population': '2.1 juta jiwa',
        'fact': 'Dikenal sebagai Kota Cinta dan pusat mode dunia.'
    },
    'Cairo': {
        'country': 'Mesir',
        'population': '10 juta jiwa',
        'fact': 'Berlokasi dekat dengan kompleks Piramida Giza yang ikonik.'
    }
}

# 2. Loop melalui dictionary cities untuk mencetak informasi setiap kota
for city_name, city_info in cities.items():
    print(f"\nKota: {city_name.title()}")
    print(f"- Negara    : {city_info['country'].title()}")
    print(f"- Populasi  : {city_info['population']}")
    print(f"- Fakta Unik: {city_info['fact']}")