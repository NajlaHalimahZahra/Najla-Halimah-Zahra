class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
         """Inisialisasi nama restoran dan jenis masakan"""
         self.restaurant_name = restaurant_name
         self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mencetak deskripsi restoran"""
        print(f"Restoran {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Mencetak pesan bahwa restoran sudah buka"""
        print(f"{self.restaurant_name} sudah buka!")


my_restaurant = Restaurant("Pojok Senja", "Nasi Goreng Seafood")

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
print("-"*30)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()