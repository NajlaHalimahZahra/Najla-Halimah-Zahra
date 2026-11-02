# Mendefinisikan fungsi make_car dengan parameter wajib dan **car_info
def make_car(manufacturer, model_name, **car_info):
    """Menyimpan informasi tentang mobil ke dalam sebuah dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model_name
    return car_info

# Memanggil fungsi dengan data wajib dan keyword arguments tambahan
car = make_car('Mazda 3', 'hatchback', color='Soul Red Crystal Metallic', tow_package=True)

# Mencetak dictionary hasil pengembalian fungsi
print(car)