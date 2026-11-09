from test_city_function import get_city_country

def test_city_country():
    """Menguji fungsi get_city_country tanpa populasi."""
    location = get_city_country('santiago', 'chile')
    assert location == 'Santiago, Chile'

def test_city_country_population():
    """Menguji fungsi get_city_country dengan populasi."""
    location = get_city_country('santiago', 'chile', population=5000000)
    assert location == 'Santiago, Chile - Population 5000000'