# Dictionary di mana valuenya adalah list
favorite_places = {
    'Norell': ['Bandung', 'Bali', 'Lombok'],
    'Willy': ['Yogyakarta', 'Malang'],
    'Kelvin': ['Raja Ampat', 'Labuan Bajo', 'Tokyo']
}

# 2. Loop melalui dictionary favorite_places
for name, places in favorite_places.items():
    print(f"\nTempat-tempat favorit {name.title()} adalah:")
    for place in places:
        print(f"- {place.title()}")