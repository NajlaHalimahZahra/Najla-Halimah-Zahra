from city_function import get_city_country

def test_city_country():
    """Apakah kota seperti 'santiago, chile' disajikan dengan benar?"""
    samed_location = get_city_country('santiago', 'chile')
    assert samed_location == 'Santiago, Chile'