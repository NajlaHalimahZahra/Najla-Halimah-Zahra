def make_car(manufacturer, model_name, **car_info):
    """Menyimpan informasi lengkap tentang mobil ke dalam sebuah dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model_name
    return car_info


# Pemanggilan fungsi dengan kerapian argumen yang terjaga
car = make_car(
    'Mazda 3', 
    'Hatchback', 
    color='Machine Grey Metallic', 
    tow_package=True
)

print(car)