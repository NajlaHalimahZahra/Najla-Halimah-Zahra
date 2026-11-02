# Mendefinisikan fungsi city_country yang mengembalikan string terformat
def city_country(city, country):
    """Mengembalikan string berupa 'City, Country'."""
    return f"{city.title()}, {country.title()}"

# Memanggil fungsi dengan tiga pasangan berbeda dan mencetak hasilnya
place_1 = city_country('Santiago', 'Chile')
place_2 = city_country('Tokyo', 'Japan')
place_3 = city_country('Paris', 'France')

print(place_1)
print(place_2)
print(place_3)