def get_city_country(city, country, population=''):
    """Mengembalikan string terformat dengan kota, negara, dan opsional populasi."""
    if population:
        formatted_location = f"{city}, {country} - population {population}"
    else:
        formatted_location = f"{city}, {country}"
        
    return formatted_location.title()